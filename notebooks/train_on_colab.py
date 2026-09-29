# Privacy-Preserving UEBA — Google Colab Training Notebook
# ========================================================
# Train FHE-native models using Concrete ML on Google Colab's free GPU/CPU.
# Concrete ML handles everything: quantized training + FHE circuit compilation.
#
# Workflow:
#   1. Setup Environment
#   2. Download CERT v4.2 Dataset
#   3. Extract Features & Preprocess (SMOTE)
#   4. Train LR + MLP (Concrete ML, FHE-native)
#   5. Evaluate on Test Set
#   6. Run FHE Encrypted Inference
#   7. Save & Download Models

# %% [markdown]
# # 🔐 Privacy-Preserving UEBA with FHE + ML
# ## Google Colab Training Notebook (Concrete ML)
# ---
# **Mục tiêu:** Train model FHE-native bằng Concrete ML trên Google Colab,
# sau đó tải về chạy FHE Inference.
#
# **Lưu ý:** Concrete ML train model đã tối ưu sẵn cho FHE (lượng tử hóa).
# Không cần train PyTorch/sklearn riêng rồi convert.

# %% [markdown]
# ## 📦 Cell 1: Mount Drive & Clone Repo

# %%
from google.colab import drive
import os

drive.mount('/content/drive')

WORK_DIR = '/content/ueba-fhe'
os.makedirs(WORK_DIR, exist_ok=True)

# Clone repo (thay URL nếu cần)
REPO_URL = "https://github.com/WanThinnn/homomorphic-encryption-with-machine-learning.git"
if not os.path.exists(os.path.join(WORK_DIR, '.git')):
    get_ipython().system(f'git clone {REPO_URL} {WORK_DIR}')
else:
    get_ipython().system(f'cd {WORK_DIR} && git pull')

os.chdir(WORK_DIR)
print(f"Working directory: {os.getcwd()}")

# %% [markdown]
# ## 📦 Cell 2: Install Dependencies

# %%
get_ipython().system('pip install -q concrete-ml imbalanced-learn')

# Verify
import concrete.ml
print(f"Concrete ML: {concrete.ml.__version__}")

import torch
print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")

# %% [markdown]
# ## 📊 Cell 3: Download CERT v4.2 Dataset

# %%
DATA_DIR = os.path.join(WORK_DIR, "data", "cert", "raw")
PROCESSED_DIR = os.path.join(WORK_DIR, "data", "cert", "processed")

# Cache trên Google Drive
DRIVE_CACHE = "/content/drive/MyDrive/UEBA_FHE_Cache"
os.makedirs(DRIVE_CACHE, exist_ok=True)

CERT_TAR = os.path.join(DRIVE_CACHE, "r4.2.tar.bz2")
ANSWERS_TAR = os.path.join(DRIVE_CACHE, "answers.tar.bz2")

if not os.path.exists(CERT_TAR):
    print("Downloading CERT v4.2 (~1.8GB)...")
    get_ipython().system(f'wget -q --show-progress -O {CERT_TAR} "https://kilthub.cmu.edu/ndownloader/articles/7694453/versions/7"')
else:
    print(f"Dataset cached: {CERT_TAR}")

if not os.path.exists(ANSWERS_TAR):
    print("Downloading labels...")
    get_ipython().system(f'wget -q --show-progress -O {ANSWERS_TAR} "https://kilthub.cmu.edu/ndownloader/articles/7694522/versions/1"')
else:
    print(f"Labels cached: {ANSWERS_TAR}")

# Extract
os.makedirs(DATA_DIR, exist_ok=True)
R42_DIR = os.path.join(DATA_DIR, "r4.2")
if not os.path.exists(R42_DIR):
    print("Extracting...")
    get_ipython().system(f'tar -xjf {CERT_TAR} -C {DATA_DIR}')
    get_ipython().system(f'tar -xjf {ANSWERS_TAR} -C {DATA_DIR}')
else:
    print(f"Already extracted: {R42_DIR}")

# %% [markdown]
# ## 🔧 Cell 4: Feature Extraction & Preprocessing

# %%
import sys
sys.path.insert(0, os.path.join(WORK_DIR, "src"))

import numpy as np

# Feature extraction
FEATURES_CSV = os.path.join(PROCESSED_DIR, "behavioral_features.csv")
if not os.path.exists(FEATURES_CSV):
    print("Extracting features from raw logs...")
    from data.adapters.cert_adapter import extract_features
    extract_features(raw_dir=R42_DIR, output_dir=PROCESSED_DIR)
else:
    print("Features already extracted. Skipping...")

# Preprocessing (SMOTE)
TRAIN_NPY = os.path.join(PROCESSED_DIR, "X_train.npy")
if not os.path.exists(TRAIN_NPY):
    print("Preprocessing (split + normalize + SMOTE)...")
    from data.cert_preprocessor import preprocess
    preprocess(data_dir=PROCESSED_DIR)
else:
    print("Preprocessed data exists. Skipping...")

# Verify
X_train = np.load(os.path.join(PROCESSED_DIR, "X_train.npy"))
y_train = np.load(os.path.join(PROCESSED_DIR, "y_train.npy"))
X_test = np.load(os.path.join(PROCESSED_DIR, "X_test.npy"))
y_test = np.load(os.path.join(PROCESSED_DIR, "y_test.npy"))
print(f"\nData ready!")
print(f"  Train: {X_train.shape} | Normal={np.sum(y_train==0)}, Malicious={np.sum(y_train==1)}")
print(f"  Test:  {X_test.shape}  | Normal={np.sum(y_test==0)}, Malicious={np.sum(y_test==1)}")

# %% [markdown]
# ## 🧠 Cell 5: Train Logistic Regression (Concrete ML)

# %%
from ml.ueba_concrete_ml import train_model

MODEL_DIR = os.path.join(WORK_DIR, "src", "ml", "models")

print("=" * 60)
print("Training Concrete ML LogisticRegression (8-bit quantized)...")
print("=" * 60)
train_model(model_type="lr", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR)
print("\nLR model trained + FHE circuit compiled + saved!")

# %% [markdown]
# ## 🧠 Cell 6: Train MLP (Concrete ML)

# %%
print("=" * 60)
print("Training Concrete ML NeuralNetClassifier (3-bit quantized)...")
print("=" * 60)
train_model(model_type="mlp", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR, epochs=15)
print("\nMLP model trained + FHE circuit compiled + saved!")

# %% [markdown]
# ## 📊 Cell 7: Evaluate on Test Set

# %%
from ml.ueba_concrete_ml import evaluate_model

print("=" * 60)
print("  LOGISTIC REGRESSION")
print("=" * 60)
evaluate_model(model_type="lr", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR)

print("\n")
print("=" * 60)
print("  MLP")
print("=" * 60)
evaluate_model(model_type="mlp", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR)

# %% [markdown]
# ## 🔐 Cell 8: FHE Encrypted Inference

# %%
from ml.ueba_concrete_ml import run_fhe_inference

print("Running REAL FHE inference (data encrypted -> compute on ciphertext -> decrypt result)")
print("Each sample takes ~0.3-1 second\n")

run_fhe_inference(model_type="mlp", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR, n_samples=10)

# %% [markdown]
# ## 💾 Cell 9: Save to Google Drive

# %%
import shutil

DRIVE_MODELS = os.path.join(DRIVE_CACHE, "trained_models")
os.makedirs(DRIVE_MODELS, exist_ok=True)

for model_name in ["ueba_lr", "ueba_mlp"]:
    src = os.path.join(MODEL_DIR, model_name)
    dst = os.path.join(DRIVE_MODELS, model_name)
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Saved {model_name} to Google Drive")

for fname in ["scaler.pkl", "feature_names.json"]:
    src = os.path.join(PROCESSED_DIR, fname)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DRIVE_MODELS, fname))

print(f"\nAll models saved to: {DRIVE_MODELS}")

# %% [markdown]
# ## 📥 Cell 10: Download as ZIP

# %%
import shutil
from google.colab import files

shutil.make_archive("/content/ueba_models", 'zip', MODEL_DIR)
files.download("/content/ueba_models.zip")
print("Download started! Extract to src/ml/models/ in your local project.")
