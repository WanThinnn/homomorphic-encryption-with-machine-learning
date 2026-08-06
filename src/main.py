import sys
import logging
from typing import List
import os

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from crypto.homomorphic_encryption import FHEPipeline
from ml.linear_model import EncryptedLinearRegression

def calculate_plaintext_prediction(inputs: List[float], weights: List[float], bias: float) -> float:
    """Tính toán Linear Regression thông thường (không mã hóa) để đối chiếu."""
    dot_product = sum(i * w for i, w in zip(inputs, weights))
    return dot_product + bias

def text_to_vector(text: str) -> List[float]:
    """Chuyển đổi văn bản thành vector các mã ASCII."""
    return [float(ord(c)) for c in text]

def main():
    print("\n" + "="*60)
    print("DEMO BẢO MẬT MÃ HÓA ĐỒNG CẤU (FHE) VỚI MACHINE LEARNING")
    print("="*60)
    
    # --- 1. Tương tác: Load hay Tạo Key ---
    fhe = FHEPipeline(mult_depth=5, scale_mod_size=40, batch_size=0) # batch_size=0 để tự động (max)
    
    secrets_dir = os.path.join(os.path.dirname(__file__), "secrets")
    priv_enc_path = os.path.join(secrets_dir, "private_key.enc")
    
    if os.path.exists(priv_enc_path):
        print("\n[HỆ THỐNG] Đã tìm thấy khóa FHE đã lưu.")
        choice = input("Bạn muốn (1) Load khóa cũ, hay (2) Tạo khóa mới (ghi đè)? [1/2]: ").strip()
        if choice == '1':
            pin = input("Vui lòng nhập mã PIN (8 ký tự) để giải mã Private Key: ").strip()
            if not fhe.load_keys(pin, secrets_dir):
                print("[!] Lỗi giải mã hoặc sai PIN. Thoát chương trình.")
                return
        else:
            print("\n[HỆ THỐNG] Đang tạo cặp khóa Public / Private mới...")
            fhe.generate_keys()
            pin = input("Tạo mã PIN (8 ký tự) để bảo vệ Private Key của bạn: ").strip()
            fhe.save_keys(pin, secrets_dir)
    else:
        print("\n[HỆ THỐNG] Chưa có khóa FHE. Đang khởi tạo khóa mới...")
        fhe.generate_keys()
        pin = input("Tạo mã PIN (8 ký tự) để bảo vệ Private Key của bạn: ").strip()
        fhe.save_keys(pin, secrets_dir)
        
    # --- 2. Tương tác: Nhập dữ liệu Text ---
    print("\n" + "-"*60)
    print("Mô hình ML hiện tại là một Linear Regression tính 'Độ phức tạp văn bản'.")
    print("Mỗi ký tự sẽ được chuyển thành mã ASCII, sau đó nhân với một trọng số cố định (0.01) và cộng với Bias.")
    print("-" * 60)
    
    user_text = input("\nNhập một đoạn text bạn muốn phân tích: ").strip()
    if not user_text:
        user_text = "Hello FHE"
        print(f"Không có đầu vào, dùng mặc định: '{user_text}'")
        
    # Chuyển thành vector
    client_input = text_to_vector(user_text)
    vector_dim = len(client_input)
    fhe.vector_dim = vector_dim  # Dynamic theo length của input
    
    # --- 3. Client mã hóa và gửi ---
    print("\n[CLIENT] Đang mã hóa vector dữ liệu... (Không ai có thể đọc được)")
    encrypted_input = fhe.encrypt_vector(client_input)
    print("[CLIENT] Hoàn tất mã hóa.")
    
    # --- 4. Server xử lý ---
    print("\n[SERVER] Nhận dữ liệu mã hóa từ Client...")
    print(f"[SERVER] Kích thước dữ liệu động nhận được: {vector_dim} chiều.")
    
    # Server tạo trọng số phù hợp với kích thước dữ liệu (Dynamic weights)
    weights = [0.01] * vector_dim
    bias = 1.5
    
    model = EncryptedLinearRegression(weights=weights, bias=bias)
    
    print("[SERVER] Đang chạy mô hình Học Máy trên dữ liệu ĐÃ MÃ HÓA...")
    encrypted_prediction = model.predict_encrypted(encrypted_input, fhe)
    print("[SERVER] Hoàn thành. Gửi trả kết quả mã hóa về Client.")
    
    # --- 5. Client giải mã ---
    print("\n[CLIENT] Nhận kết quả từ Server và giải mã bằng Private Key...")
    decrypted_result = fhe.decrypt_vector(encrypted_prediction)
    fhe_final_value = decrypted_result[0]
    
    print("\n" + "="*60)
    print("KẾT QUẢ SO SÁNH")
    print("="*60)
    expected_value = calculate_plaintext_prediction(client_input, weights, bias)
    
    print(f"Text đầu vào: '{user_text}'")
    print(f"Dự đoán mong đợi (Plaintext): {expected_value:.4f}")
    print(f"Dự đoán bằng FHE (Ciphertext): {fhe_final_value:.4f}")
    print(f"Sai số: {abs(expected_value - fhe_final_value):.6f}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
