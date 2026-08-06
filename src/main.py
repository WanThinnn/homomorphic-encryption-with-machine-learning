import sys
import logging
from typing import List

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Thêm thư mục lib vào sys.path để có thể load module openfhe
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from crypto.homomorphic_encryption import FHEPipeline
from ml.linear_model import EncryptedLinearRegression

def calculate_plaintext_prediction(inputs: List[float], weights: List[float], bias: float) -> float:
    """Tính toán Linear Regression thông thường (không mã hóa) để đối chiếu."""
    dot_product = sum(i * w for i, w in zip(inputs, weights))
    return dot_product + bias

def main():
    logger.info("=== BẮT ĐẦU DEMO FHE + MACHINE LEARNING (LINEAR REGRESSION) ===")
    
    # 1. Cấu hình bài toán
    vector_dim = 4 # Kích thước linh hoạt như bạn yêu cầu
    
    weights = [0.5, 1.2, -0.8, 2.1]
    bias = 0.5
    
    client_input = [1.5, 2.0, -1.0, 0.5]
    
    # 2. Khởi tạo FHE Pipeline (Đóng vai trò quản lý khóa và context)
    fhe = FHEPipeline(mult_depth=5, scale_mod_size=40, batch_size=vector_dim, vector_dim=vector_dim)
    
    logger.info("--- CLIENT: TẠO KHÓA VÀ MÃ HÓA DỮ LIỆU ---")
    fhe.generate_keys()
    
    encrypted_input = fhe.encrypt_vector(client_input)
    logger.info("Client đã mã hóa dữ liệu thành công.")
    
    logger.info("--- SERVER: NHẬN DỮ LIỆU MÃ HÓA VÀ CHẠY MÔ HÌNH ---")
    # Khởi tạo mô hình trên server
    model = EncryptedLinearRegression(weights=weights, bias=bias)
    
    # Chạy inference trực tiếp trên dữ liệu mã hóa
    encrypted_prediction = model.predict_encrypted(encrypted_input, fhe)
    logger.info("Server đã hoàn thành dự đoán trên Ciphertext.")
    
    logger.info("--- CLIENT: NHẬN KẾT QUẢ MÃ HÓA VÀ GIẢI MÃ ---")
    # Client nhận kết quả và giải mã bằng Private Key
    decrypted_result = fhe.decrypt_vector(encrypted_prediction)
    
    # Kết quả EvalSum thường nằm ở tất cả các slot hoặc slot đầu tiên, ta lấy slot đầu
    fhe_final_value = decrypted_result[0]
    
    logger.info("--- TỔNG KẾT & SO SÁNH ---")
    expected_value = calculate_plaintext_prediction(client_input, weights, bias)
    logger.info(f"Dữ liệu đầu vào: {client_input}")
    logger.info(f"Trọng số mô hình: {weights}, Bias: {bias}")
    logger.info(f"Dự đoán mong đợi (Plaintext): {expected_value:.4f}")
    logger.info(f"Dự đoán bằng FHE (Ciphertext): {fhe_final_value:.4f}")
    
    diff = abs(expected_value - fhe_final_value)
    logger.info(f"Sai số (Precision error do FHE): {diff:.6f}")
    
    if diff < 0.01:
        logger.info("=> THÀNH CÔNG: Kết quả FHE hoàn toàn khớp với kết quả thông thường!")
    else:
        logger.warning("=> CẢNH BÁO: Sai số lớn hơn bình thường.")

if __name__ == "__main__":
    main()
