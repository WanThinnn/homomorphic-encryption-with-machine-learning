# Privacy-Preserving UEBA — Google Colab Training Notebook
# ========================================================
# Train FHE-native models using Concrete ML on Google Colab's free GPU/CPU.
# Concrete ML handles everything: quantized training + FHE circuit compilation.
#
# Workflow:
#   1. Setup Environment
#   2. Install Python 3.10 (Compatible with Concrete ML)
#   3. Download CERT v4.2 Dataset
#   4. Train LR + MLP (Concrete ML, FHE-native)
#   5. Evaluate on Test Set
#   6. Run FHE Encrypted Inference
#   7. Save Models

# %% [markdown]
# # 🔐 Privacy-Preserving UEBA with FHE + ML
# ## Google Colab Training Notebook (Concrete ML)
# ---
# **Lưu ý Quan Trọng:** Google Colab hiện tại dùng Python 3.12+, nhưng `concrete-ml` chỉ hỗ trợ tối đa Python 3.11.
# Notebook này sẽ tự động cài đặt **Python 3.10** và chạy các lệnh thông qua CLI để đảm bảo tương thích 100%.

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
# ## 🐍 Cell 2: Install Python 3.10 & Dependencies
# Chúng ta sẽ cài Python 3.10 và cài `concrete-ml` vào đó.

# %%
%%bash
# Cài đặt Python 3.10
sudo apt-get update -y
sudo apt-get install python3.10 python3.10-distutils -y

# Cài pip cho Python 3.10
curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py --ignore-installed

# Cài đặt thư viện ML và PyTorch
python3.10 -m pip install -q concrete-ml imbalanced-learn torch torchvision scikit-learn pandas numpy --ignore-installed

# Cài đặt backend CUDA cho Concrete FHE (Tăng tốc FHE Compile & Inference bằng GPU)
python3.10 -m pip install -q concrete-python --index-url https://pypi.zama.ai/gpu --trusted-host pypi.zama.ai --ignore-installed

# Kiểm tra version
python3.10 -c "import concrete.ml; print('Concrete ML version:', concrete.ml.__version__)"

# %% [markdown]
# ## 📊 Cell 3: Prepare Dataset
# Download (nếu chưa có) và trích xuất đặc trưng + SMOTE.

# %%
import os

DATA_DIR = os.path.join(WORK_DIR, "data", "cert", "raw")
DRIVE_DATASET = "/content/drive/MyDrive/Colab Notebooks"
CERT_TAR = os.path.join(DRIVE_DATASET, "r4.2.tar.bz2")
ANSWERS_TAR = os.path.join(DRIVE_DATASET, "answers.tar.bz2")

if os.path.exists(CERT_TAR):
    print(f"Dataset found on Drive: {CERT_TAR}")
else:
    print(f"WARNING: Dataset not found at {CERT_TAR}")
    print("Downloading CERT v4.2 (~1.8GB)...")
    os.makedirs(DRIVE_DATASET, exist_ok=True)
    get_ipython().system(f'wget -q --show-progress -O "{CERT_TAR}" "https://kilthub.cmu.edu/ndownloader/articles/7694453/versions/7"')

if os.path.exists(ANSWERS_TAR):
    print(f"Labels found on Drive: {ANSWERS_TAR}")
else:
    print(f"WARNING: Labels not found at {ANSWERS_TAR}")
    print("Downloading labels...")
    get_ipython().system(f'wget -q --show-progress -O "{ANSWERS_TAR}" "https://kilthub.cmu.edu/ndownloader/articles/7694522/versions/1"')

# Extract
os.makedirs(DATA_DIR, exist_ok=True)
R42_DIR = os.path.join(DATA_DIR, "r4.2")
if not os.path.exists(R42_DIR):
    print("Extracting dataset...")
    get_ipython().system(f'tar -xjf "{CERT_TAR}" -C {DATA_DIR}')
    get_ipython().system(f'tar -xjf "{ANSWERS_TAR}" -C {DATA_DIR}')
    print("Extraction complete!")
else:
    print(f"Already extracted: {R42_DIR}")

# Chạy tiền xử lý (Extract Features + SMOTE) bằng Python 3.10
get_ipython().system('python3.10 src/main.py prepare-data')

# %% [markdown]
# ## 🧠 Cell 4: Train Logistic Regression (Concrete ML)

# %%
get_ipython().system('python3.10 src/main.py train --model lr')

# %% [markdown]
# ## 🧠 Cell 5: Train MLP (Concrete ML)
# 4-bit quantization, 3 hidden layers, 50 epochs. Quá trình này sẽ mất vài phút.

# %%
get_ipython().system('python3.10 src/main.py train --model mlp --epochs 50')

# %% [markdown]
# ## 📊 Cell 6: Evaluate on Test Set

# %%
print("=== LOGISTIC REGRESSION ===")
get_ipython().system('python3.10 src/main.py evaluate --model lr')

print("\n=== MLP ===")
get_ipython().system('python3.10 src/main.py evaluate --model mlp')

# %% [markdown]
# ## 🔐 Cell 7: FHE Encrypted Inference
# Test chạy inference mã hóa thực tế trên model đã compile.

# %%
get_ipython().system('python3.10 src/main.py fhe-inference --model mlp --n-samples 10')

# %% [markdown]
# ## 💾 Cell 8: Save to Google Drive

# %%
import shutil

PROCESSED_DIR = os.path.join(WORK_DIR, "data", "cert", "processed")
MODEL_DIR = os.path.join(WORK_DIR, "src", "ml", "models")
DRIVE_MODELS = os.path.join(DRIVE_DATASET, "trained_models")
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
# ## 📥 Cell 9: Download as ZIP (Tùy chọn)

# %%
import shutil
from google.colab import files

shutil.make_archive("/content/ueba_models", 'zip', MODEL_DIR)
files.download("/content/ueba_models.zip")
print("Download started! Extract to src/ml/models/ in your local project.")
