import os
import sys
import json
import logging
import math

# Thêm thư mục dự án vào sys.path để import được src...
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
base_dir = os.path.dirname(src_dir)
sys.path.append(base_dir)

# Thêm src/lib để import openfhe.pyd
sys.path.append(os.path.join(src_dir, "lib"))

from src.crypto.homomorphic_encryption import FHEPipeline
from src.ml.linear_model import EncryptedLinearRegression

logging.basicConfig(level=logging.INFO, format='%(asctime)s - FHE_WORKER - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_fhe_pipeline(pin: str):
    secrets_dir = os.path.join(src_dir, "secrets")
    models_dir = os.path.join(src_dir, "ml", "models")
    tmp_dir = os.path.join(base_dir, "tmp")
    
    # Đọc dữ liệu đã được Vector hóa từ Client
    client_input_path = os.path.join(tmp_dir, "client_input.json")
    if not os.path.exists(client_input_path):
        logger.error(f"Không tìm thấy {client_input_path}")
        return
        
    with open(client_input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        vector = data['vector']
        
    # Khởi tạo FHE
    # Chú ý: vector_dim phải khớp với max_features của Vectorizer (ở đây là 256)
    vector_dim = len(vector)
    logger.info(f"Khởi tạo FHEPipeline với vector_dim={vector_dim} (batch_size=0 full packing)")
    fhe = FHEPipeline(mult_depth=5, scale_mod_size=40, batch_size=0, vector_dim=vector_dim)
    
    # Nạp khóa
    try:
        if not fhe.load_keys(pin, secrets_dir):
            logger.warning("Chưa có khóa FHE. Đang tạo khóa mới...")
            fhe.generate_keys()
            fhe.save_keys(pin, secrets_dir)
    except Exception as e:
        logger.error(f"Dừng chương trình do lỗi nạp khóa: {e}")
        sys.exit(1)
        
    # ==========================================
    # [CLIENT] MÃ HÓA
    # ==========================================
    logger.info("[CLIENT] Đang mã hóa vector dữ liệu thật...")
    enc_vector = fhe.encrypt_vector(vector)
    
    # Xuất file ciphertext ra để user xem
    import openfhe
    ct_path = os.path.join(tmp_dir, "client_ciphertext.bin")
    openfhe.SerializeToFile(ct_path, enc_vector, openfhe.BINARY)
    logger.info(f"[CLIENT] Đã xuất file Ciphertext mẫu ra: {ct_path}")
    
    # ==========================================
    # [SERVER] INFERENCE TRÊN DỮ LIỆU MÃ HÓA
    # ==========================================
    logger.info("[SERVER] Đang nạp Trọng số (Weights) từ mô hình thật...")
    weights_path = os.path.join(models_dir, "weights.json")
    with open(weights_path, 'r', encoding='utf-8') as f:
        model_data = json.load(f)
        weights = model_data['weights']
        bias = model_data['bias']
        
    model = EncryptedLinearRegression(weights=weights, bias=bias)
    model.precompute(fhe)
    
    logger.info("[SERVER] Đang tính toán Hồi quy tuyến tính trên Ciphertext...")
    enc_result = model.predict_encrypted(enc_vector, fhe)
    
    # ==========================================
    # [CLIENT] GIẢI MÃ
    # ==========================================
    logger.info("[CLIENT] Đang giải mã kết quả...")
    decrypted_vec = fhe.decrypt_vector(enc_result)
    
    # Kết quả của EvalSum nằm ở tất cả các slot, ta lấy phần tử đầu tiên
    logit = decrypted_vec[0]
    
    result_path = os.path.join(tmp_dir, "result.json")
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump({"logit": logit}, f)
    
    logger.info("[CLIENT] Hoàn tất! Đã lưu kết quả giải mã.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fhe_worker.py <pin>")
        sys.exit(1)
    pin = sys.argv[1]
    run_fhe_pipeline(pin)
