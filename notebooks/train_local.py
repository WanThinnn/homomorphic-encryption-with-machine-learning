# %% [markdown]
# # Phân tích hành vi người dùng (UEBA) với Máy học đồng hình (FHE)
# ## Môi trường Local (WSL2 + NVIDIA RTX 3050)
# Notebook này được tối ưu để chạy trên máy tính cá nhân.
#
# **Yêu cầu trước khi chạy:**
# 1. Bạn đã kích hoạt môi trường ảo: `source concrete_ml_env/bin/activate`
# 2. Bạn đã copy 2 file `r4.2.tar.bz2` và `answers.tar.bz2` vào thư mục `data/cert/raw/` của dự án.

# %%
import os

# Đảm bảo thư mục làm việc là thư mục gốc của dự án
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir("..")
print(f"Working directory: {os.getcwd()}")

# Cấu hình đường dẫn dữ liệu
DATA_DIR = os.path.join("data", "cert", "raw")
CERT_TAR = os.path.join(DATA_DIR, "r4.2.tar.bz2")
ANSWERS_TAR = os.path.join(DATA_DIR, "answers.tar.bz2")
R42_DIR = os.path.join(DATA_DIR, "r4.2")

# %% [markdown]
# ## 📦 Cell 1: Giải nén Dataset
# Nếu bạn chưa giải nén dataset, cell này sẽ tự động giải nén.

# %%
if not os.path.exists(R42_DIR):
    if not os.path.exists(CERT_TAR) or not os.path.exists(ANSWERS_TAR):
        print(f"LỖI: Không tìm thấy dataset gốc tại {DATA_DIR}!")
        print("Vui lòng tải r4.2.tar.bz2 và answers.tar.bz2 bỏ vào thư mục data/cert/raw/")
    else:
        print("Đang giải nén dữ liệu... (sẽ mất vài phút)")
        get_ipython().system(f'tar -xjf "{CERT_TAR}" -C "{DATA_DIR}"')
        get_ipython().system(f'tar -xjf "{ANSWERS_TAR}" -C "{DATA_DIR}"')
        print("Giải nén hoàn tất!")
else:
    print(f"Dữ liệu đã được giải nén sẵn tại: {R42_DIR}")

# %% [markdown]
# ## 🧹 Cell 2: Chuẩn bị Dữ liệu (Trích xuất đặc trưng & SMOTE)
# Đọc các log file nặng hàng GB, tính toán tần suất hành vi, gán nhãn Độc hại và dùng SMOTE cân bằng dữ liệu.
# (Có thể mất 5-10 phút để chạy qua hàng triệu dòng log).

# %%
get_ipython().system('python3 src/main.py prepare-data')

# %% [markdown]
# ## 🧠 Cell 3: Huấn luyện Mô hình Neural Network (PyTorch + CUDA)
# Quá trình này sẽ sử dụng trực tiếp sức mạnh của card **RTX 3050** thông qua cờ `device="cuda"`.

# %%
get_ipython().system('python3 src/main.py train --model mlp --epochs 50')

# %% [markdown]
# ## 📊 Cell 4: Đánh giá mô hình (Tùy chọn)

# %%
get_ipython().system('python3 src/main.py evaluate --model mlp')

# %% [markdown]
# ## 🔐 Cell 5: FHE Inference (Thực thi Mã hóa Đồng hình)
# Mạch FHE sẽ được biên dịch và chạy trên CPU đa luồng để dự đoán các mẫu ẩn danh.

# %%
get_ipython().system('python3 src/main.py fhe-inference --model mlp')
