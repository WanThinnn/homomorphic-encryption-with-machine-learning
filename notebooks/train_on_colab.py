# Privacy-Preserving UEBA — Google Colab Training Notebook
# ========================================================
# This notebook allows you to train UEBA models on Google Colab's free GPU,
# then download the trained models to run FHE inference locally.
#
# Steps:
#   1. Mount Google Drive & Clone Repo
#   2. Install Dependencies
#   3. Download & Prepare CERT v4.2 Dataset
#   4. Train Models (LR + MLP) on GPU
#   5. Evaluate Models
#   6. Run Concrete ML FHE Inference
#   7. Download Trained Models

# %% [markdown]
# # 🔐 Privacy-Preserving UEBA with FHE + ML
# ## Google Colab Training Notebook
# ---
# **Mục tiêu:** Train mô hình Machine Learning trên GPU miễn phí của Google Colab,
# sau đó tải về máy local để chạy FHE Inference.

# %% [markdown]
# ## 📦 Cell 1: Setup Environment

# %%
# ============================================================
# CELL 1: Mount Google Drive & Clone Repository
# ============================================================
from google.colab import drive
import os

# Mount Google Drive để lưu trữ dataset và model
drive.mount('/content/drive')

# Tạo thư mục làm việc
WORK_DIR = '/content/ueba-fhe'
if not os.path.exists(WORK_DIR):
    os.makedirs(WORK_DIR)

# Clone repository (thay YOUR_REPO_URL bằng URL thực tế)
REPO_URL = "https://github.com/WanThinnn/homomorphic-encryption-with-machine-learning.git"
if not os.path.exists(os.path.join(WORK_DIR, '.git')):
    !git clone {REPO_URL} {WORK_DIR}
else:
    !cd {WORK_DIR} && git pull

os.chdir(WORK_DIR)
print(f"Working directory: {os.getcwd()}")
!ls -la

# %% [markdown]
# ## 📦 Cell 2: Install Dependencies

# %%
# ============================================================
# CELL 2: Install Dependencies
# ============================================================
!pip install -q torch torchvision --index-url https://download.pytorch.org/whl/cu121
!pip install -q scikit-learn pandas numpy imbalanced-learn concrete-ml

# Verify GPU
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB")

# %% [markdown]
# ## 📊 Cell 3: Download CERT v4.2 Dataset

# %%
# ============================================================
# CELL 3: Download & Extract CERT v4.2 Dataset
# ============================================================
import os

DATA_DIR = os.path.join(WORK_DIR, "data", "cert", "raw")
PROCESSED_DIR = os.path.join(WORK_DIR, "data", "cert", "processed")

# Check if dataset already exists in Google Drive (to avoid re-downloading)
DRIVE_CACHE = "/content/drive/MyDrive/UEBA_FHE_Cache"
os.makedirs(DRIVE_CACHE, exist_ok=True)

CERT_TAR = os.path.join(DRIVE_CACHE, "r4.2.tar.bz2")
ANSWERS_TAR = os.path.join(DRIVE_CACHE, "answers.tar.bz2")

if not os.path.exists(CERT_TAR):
    print("Downloading CERT v4.2 dataset (~1.8GB)... This may take 5-10 minutes.")
    !wget -q --show-progress -O {CERT_TAR} "https://kilthub.cmu.edu/ndownloader/articles/7694453/versions/7"
else:
    print(f"Dataset found in Google Drive cache: {CERT_TAR}")

if not os.path.exists(ANSWERS_TAR):
    print("Downloading answers/labels...")
    !wget -q --show-progress -O {ANSWERS_TAR} "https://kilthub.cmu.edu/ndownloader/articles/7694522/versions/1"
else:
    print(f"Answers found in Google Drive cache: {ANSWERS_TAR}")

# Extract
os.makedirs(DATA_DIR, exist_ok=True)
R42_DIR = os.path.join(DATA_DIR, "r4.2")
if not os.path.exists(R42_DIR):
    print("Extracting dataset...")
    !tar -xjf {CERT_TAR} -C {DATA_DIR}
    !tar -xjf {ANSWERS_TAR} -C {DATA_DIR}
    print("Extraction complete!")
else:
    print(f"Dataset already extracted at {R42_DIR}")

!ls {R42_DIR}

# %% [markdown]
# ## 🔧 Cell 4: Feature Extraction & Preprocessing

# %%
# ============================================================
# CELL 4: Extract Features & Preprocess (SMOTE)
# ============================================================
import sys
sys.path.insert(0, os.path.join(WORK_DIR, "src"))

# Check if features already extracted
FEATURES_CSV = os.path.join(PROCESSED_DIR, "behavioral_features.csv")
if os.path.exists(FEATURES_CSV):
    print(f"Features already extracted at {FEATURES_CSV}. Skipping...")
else:
    print("Extracting behavioral features from raw logs...")
    from data.adapters.cert_adapter import extract_features
    extract_features(raw_dir=R42_DIR, output_dir=PROCESSED_DIR)

# Preprocess (normalize + SMOTE)
TRAIN_NPY = os.path.join(PROCESSED_DIR, "X_train.npy")
if os.path.exists(TRAIN_NPY):
    print(f"Preprocessed data already exists. Skipping...")
else:
    print("Preprocessing (normalize, split, SMOTE)...")
    from data.cert_preprocessor import preprocess
    preprocess(data_dir=PROCESSED_DIR)

# Verify
import numpy as np
X_train = np.load(os.path.join(PROCESSED_DIR, "X_train.npy"))
y_train = np.load(os.path.join(PROCESSED_DIR, "y_train.npy"))
X_test = np.load(os.path.join(PROCESSED_DIR, "X_test.npy"))
y_test = np.load(os.path.join(PROCESSED_DIR, "y_test.npy"))
print(f"\n✅ Data ready!")
print(f"  Train: {X_train.shape} | Normal: {np.sum(y_train==0)}, Malicious: {np.sum(y_train==1)}")
print(f"  Test:  {X_test.shape}  | Normal: {np.sum(y_test==0)}, Malicious: {np.sum(y_test==1)}")

# %% [markdown]
# ## 🧠 Cell 5: Train Logistic Regression

# %%
# ============================================================
# CELL 5: Train Logistic Regression
# ============================================================
from ml.ueba_baseline import train_model

print("Training Logistic Regression...")
train_model(
    model_type="lr",
    data_dir=PROCESSED_DIR,
    output_dir=os.path.join(WORK_DIR, "src", "ml", "models"),
    epochs=100,  # not used for LR but required by API
)
print("\n✅ LR model saved!")

# %% [markdown]
# ## 🧠 Cell 6: Train MLP (GPU Accelerated)

# %%
# ============================================================
# CELL 6: Train MLP on GPU
# ============================================================
import torch
print(f"Training MLP on: {'GPU (' + torch.cuda.get_device_name(0) + ')' if torch.cuda.is_available() else 'CPU'}")

train_model(
    model_type="mlp",
    data_dir=PROCESSED_DIR,
    output_dir=os.path.join(WORK_DIR, "src", "ml", "models"),
    epochs=100,
)
print("\n✅ MLP model saved!")

# %% [markdown]
# ## 📊 Cell 7: Evaluate Models on Test Set

# %%
# ============================================================
# CELL 7: Evaluate Both Models
# ============================================================
from ml.ueba_baseline import evaluate_model

MODEL_DIR = os.path.join(WORK_DIR, "src", "ml", "models")

print("=" * 60)
print("EVALUATING LOGISTIC REGRESSION")
print("=" * 60)
evaluate_model(model_type="lr", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR)

print("\n")
print("=" * 60)
print("EVALUATING MLP")
print("=" * 60)
evaluate_model(model_type="mlp", data_dir=PROCESSED_DIR, model_dir=MODEL_DIR)

# %% [markdown]
# ## 🔐 Cell 8: Concrete ML FHE Inference (TFHE)

# %%
# ============================================================
# CELL 8: FHE Inference with Concrete ML
# ============================================================
from ml.ueba_concrete_ml import run_concrete_inference

print("Running FHE inference (Concrete ML / TFHE)...")
print("This will: Train quantized model -> Compile FHE circuit -> Run encrypted inference")
print("Expected time: 3-5 minutes\n")

run_concrete_inference(
    model_type="mlp",
    data_dir=PROCESSED_DIR,
    model_dir=MODEL_DIR,
    n_samples=10,
)

# %% [markdown]
# ## 💾 Cell 9: Save Models to Google Drive

# %%
# ============================================================
# CELL 9: Copy Trained Models to Google Drive
# ============================================================
import shutil

DRIVE_MODELS = os.path.join(DRIVE_CACHE, "trained_models")
os.makedirs(DRIVE_MODELS, exist_ok=True)

# Copy model files
src_models = os.path.join(WORK_DIR, "src", "ml", "models")
for model_name in ["ueba_lr", "ueba_mlp"]:
    src = os.path.join(src_models, model_name)
    dst = os.path.join(DRIVE_MODELS, model_name)
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Copied {model_name} to Google Drive")

# Also copy preprocessed data (scaler, feature_names)
for fname in ["scaler.pkl", "feature_names.json"]:
    src = os.path.join(PROCESSED_DIR, fname)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DRIVE_MODELS, fname))

print(f"\nAll models saved to: {DRIVE_MODELS}")
print("You can download them from Google Drive to your local machine.")

# %% [markdown]
# ## 📥 Cell 10: Download Models Directly (Alternative)

# %%
# ============================================================
# CELL 10: Download trained models as ZIP
# ============================================================
import shutil
from google.colab import files

# Create ZIP of all models
ZIP_NAME = "ueba_trained_models"
shutil.make_archive(
    os.path.join("/content", ZIP_NAME),
    'zip',
    os.path.join(WORK_DIR, "src", "ml", "models")
)

# Trigger browser download
print("Downloading trained models as ZIP...")
files.download(f"/content/{ZIP_NAME}.zip")
print("Download started! Save the ZIP and extract to src/ml/models/ in your local project.")
