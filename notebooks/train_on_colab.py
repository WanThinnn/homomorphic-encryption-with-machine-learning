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
# Cài đặt Python 3.10 và venv để tạo môi trường cách ly hoàn toàn
sudo apt-get update -y
sudo apt-get install python3.10 python3.10-venv python3.10-distutils -y

# Tạo môi trường ảo có tên colab_env để tránh xung đột thư viện mặc định của Colab
python3.10 -m venv colab_env
source colab_env/bin/activate

# Cập nhật pip trong venv
pip install --upgrade pip

# 1. Cài đặt các thư viện ML cơ bản và concrete-ml (Bản CPU mặc định)
pip install -q numpy pandas scikit-learn torch imbalanced-learn concrete-ml==1.9.0

# 2. Xóa bỏ lõi compiler CPU mặc định
pip uninstall -y concrete-python concrete-compiler

# 3. Cài đặt lõi compiler GPU (CUDA 11.8/12.x) tương thích chính xác với concrete-ml 1.9.0
pip install -q concrete-python==2.10.0 --extra-index-url https://pypi.zama.ai/gpu

# Kiểm tra version
python -c "import concrete.ml; print('Concrete ML version:', concrete.ml.__version__)"

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
get_ipython().system('source colab_env/bin/activate && python src/main.py prepare-data')

# %% [markdown]
# ## 🧠 Cell 4: Train Logistic Regression (Concrete ML)

# %%
get_ipython().system('source colab_env/bin/activate && python src/main.py train --model lr')

# %% [markdown]
# ## 🧠 Cell 5: Train MLP (Concrete ML)
# 4-bit quantization, 3 hidden layers, 50 epochs. Quá trình này sẽ mất vài phút.

# %%
get_ipython().system('source colab_env/bin/activate && python src/main.py train --model mlp --epochs 50')

# %% [markdown]
# ## 📊 Cell 6: Evaluate on Test Set

# %%
print("=== LOGISTIC REGRESSION ===")
get_ipython().system('source colab_env/bin/activate && python src/main.py evaluate --model lr')

print("\n=== MLP ===")
get_ipython().system('source colab_env/bin/activate && python src/main.py evaluate --model mlp')

# %% [markdown]
# ## 🔐 Cell 7: FHE Encrypted Inference
# Test chạy inference mã hóa thực tế trên model đã compile.

# %%
get_ipython().system('source colab_env/bin/activate && python src/main.py fhe-inference --model mlp --n-samples 10')

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

# %% [markdown]
# ## 🏠 Cell 10: (Tùy chọn) Chạy Local trên WSL với NVIDIA RTX 3050
# Nếu bạn chạy file `.ipynb` này trên máy tính cá nhân (WSL2) có card **RTX 3050**, bạn **BỎ QUA Cell 1 và Cell 2**.
# Mở terminal trên WSL, kích hoạt môi trường ảo: `source concrete_ml_env/bin/activate`.
# 
# Bạn có thể chạy trực tiếp các lệnh sau trên Jupyter Notebook mở bằng WSL:

# %%
# Uncomment các dòng dưới đây để chạy full pipeline (sử dụng python3 thay vì python3.10)

# !python3 src/main.py prepare-data
# !python3 src/main.py train --model mlp --epochs 50
# !python3 src/main.py evaluate --model lr
# !python3 src/main.py fhe-inference --model mlp
