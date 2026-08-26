import os
import sys
import logging
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from concrete.ml.deployment import FHEModelServer
except ImportError:
    print("Vui lòng cài đặt concrete-ml trên Linux/WSL (pip install concrete-ml)")
    sys.exit(1)

from fhe_io import read_concrete_batch, write_blob_list

logging.basicConfig(level=logging.INFO, format='%(asctime)s - CONCRETE_WORKER - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main(model_name):
    src_dir = os.path.dirname(current_dir)
    base_dir = os.path.dirname(src_dir)
    
    deploy_dir = os.path.join(src_dir, "ml", "models", model_name)
    tmp_dir = os.path.join(base_dir, "tmp")
    
    if not os.path.exists(os.path.join(deploy_dir, "server.zip")):
        logger.error("Không tìm thấy server.zip trong thư mục deployment!")
        sys.exit(1)
        
    logger.info("[SERVER] Đang khởi tạo FHE Server (TFHE) từ tệp Deployment (1 lần)...")
    try:
        import concrete.compiler
        if hasattr(concrete.compiler, "check_gpu_available") and concrete.compiler.check_gpu_available():
            logger.info("[SERVER] 🚀 Đang kích hoạt tăng tốc NVIDIA GPU (CUDA)...")
    except Exception:
        pass
    server = FHEModelServer(deploy_dir)
    
    batch_path = os.path.join(tmp_dir, "concrete_enc_batch.bin")
    if not os.path.exists(batch_path):
        logger.error("Chưa nhận được batch ciphertext từ Client!")
        sys.exit(1)

    eval_keys, payloads = read_concrete_batch(batch_path)
    if not payloads:
        logger.error("Batch ciphertext rỗng.")
        sys.exit(1)

    logger.info("[SERVER] Inference %d ciphertext trên server đã nạp sẵn...", len(payloads))
    results = []
    for idx, encrypted_data in enumerate(payloads, start=1):
        logger.info("[SERVER] Mẫu %d/%d...", idx, len(payloads))
        results.append(server.run(encrypted_data, eval_keys))
    
    result_path = os.path.join(tmp_dir, "concrete_enc_results.bin")
    write_blob_list(result_path, results)
    logger.info("[SERVER] Hoàn tất! Đã lưu %d kết quả mã hóa.", len(results))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    args = parser.parse_args()
    
    main(args.model)
