import os
import sys
import logging
import argparse

try:
    from concrete.ml.deployment import FHEModelServer
except ImportError:
    print("Vui lòng cài đặt concrete-ml trên Linux/WSL (pip install concrete-ml)")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - CONCRETE_WORKER - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main(model_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(current_dir)
    base_dir = os.path.dirname(src_dir)
    
    deploy_dir = os.path.join(src_dir, "ml", "models", model_name)
    tmp_dir = os.path.join(base_dir, "tmp")
    
    if not os.path.exists(os.path.join(deploy_dir, "server.zip")):
        logger.error("Không tìm thấy server.zip trong thư mục deployment!")
        sys.exit(1)
        
    logger.info("[SERVER] Đang khởi tạo FHE Server (TFHE) từ tệp Deployment...")
    server = FHEModelServer(deploy_dir)
    
    enc_data_path = os.path.join(tmp_dir, "concrete_enc_data.bin")
    eval_keys_path = os.path.join(tmp_dir, "concrete_eval_keys.bin")
    
    if not os.path.exists(enc_data_path) or not os.path.exists(eval_keys_path):
        logger.error("Chưa nhận được Dữ liệu mã hóa hoặc Evaluation Keys từ Client!")
        sys.exit(1)
        
    logger.info("[SERVER] Đang nạp Dữ liệu và Evaluation Keys...")
    with open(enc_data_path, 'rb') as f:
        encrypted_data = f.read()
        
    with open(eval_keys_path, 'rb') as f:
        serialized_evaluation_keys = f.read()
        
    logger.info("[SERVER] Bắt đầu tính toán Inference trên Ciphertext (Bằng Mạch FHE TFHE)...")
    # Bước này hoàn toàn không giải mã dữ liệu, thực hiện tính toán mù hoàn toàn
    encrypted_result = server.run(encrypted_data, serialized_evaluation_keys)
    
    logger.info("[SERVER] Đã tính toán xong. Lưu kết quả mã hóa...")
    result_path = os.path.join(tmp_dir, "concrete_enc_result.bin")
    with open(result_path, 'wb') as f:
        f.write(encrypted_result)
        
    logger.info("[SERVER] Hoàn tất!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    args = parser.parse_args()
    
    main(args.model)
