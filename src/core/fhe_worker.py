import os
import sys
import json
import logging
import argparse
import math

# Thêm thư mục dự án vào sys.path để import được src...
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
base_dir = os.path.dirname(src_dir)
sys.path.append(base_dir)

# Thêm src/lib để import openfhe.pyd (Chỉ Windows)
if sys.platform != 'linux':
    sys.path.append(os.path.join(src_dir, "lib"))

from src.crypto.homomorphic_encryption import FHEPipeline
from src.ml.logistic_regression import LogisticRegressionServerModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - FHE_WORKER - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_fhe_pipeline(pin: str, model_name: str):
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
        
    # LR chỉ cần 1 phép nhân CKKS (W*X); depth 2 đủ cho EvalMult + margin.
    vector_dim = len(vector)
    logger.info(f"Khởi tạo FHEPipeline với vector_dim={vector_dim} (CKKS packing, mult_depth=2)")
    fhe = FHEPipeline(mult_depth=2, scale_mod_size=40, batch_size=0, vector_dim=vector_dim, init_context=False)
    
    try:
        if not fhe.load_keys(pin, secrets_dir):
            logger.warning("Chưa có khóa FHE. Đang tạo khóa mới...")
            fhe._init_context()
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
    weights_path = os.path.join(models_dir, model_name, "weights.json")
    with open(weights_path, 'r', encoding='utf-8') as f:
        model_data = json.load(f)
        weights = model_data['weights']
        bias = model_data['bias']
        
    model = LogisticRegressionServerModel(weights=weights, bias=bias)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", type=str, required=True)
    parser.add_argument("--model", type=str, required=True)
    args = parser.parse_args()
    
    run_fhe_pipeline(args.pin, args.model)
