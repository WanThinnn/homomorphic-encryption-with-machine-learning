import os
import sys
import json
import getpass
import subprocess
import argparse
import logging
import io

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - CLIENT - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Chạy Client cho mô hình FHE.")
    parser.add_argument("--model", type=str, required=True, help="Tên thư mục mô hình (vd: simple_logistic_regression, pretrained_xgb)")
    parser.add_argument("--platform", type=str, default="concrete_ml", choices=["concrete_ml", "openfhe", "none"], help="Nền tảng FHE (concrete, openfhe, hoặc none)")
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, "ml", "models")
    tmp_dir = os.path.join(base_dir, "..", "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    
    print("============================================================")
    print("     PHÂN LOẠI VỚI OPENFHE VÀ MACHINE LEARNING              ")
    print("============================================================")
    
    platform = "openfhe" if args.platform == "none" else args.platform
    
    if platform == "openfhe":
        try:
            from ml.logistic_regression import LogisticRegressionClientModel
            model = LogisticRegressionClientModel(models_dir, model_name=args.model)
        except Exception as e:
            logger.error(f"Lỗi khởi tạo mô hình OpenFHE: {e}")
            sys.exit(1)
    elif platform == "concrete_ml":
        if sys.platform != 'linux':
            logger.error("Concrete ML BẮT BUỘC phải được chạy trên WSL/Linux!")
            sys.exit(1)
        try:
            # Sử dụng Client Model chuyên biệt cho UNSW-NB15 (Intrusion Detection)
            if args.model == "unsw_nb15_xgb":
                from ml.unsw_nb15_client import UNSWNB15ClientModel
                model = UNSWNB15ClientModel(models_dir, model_name=args.model)
            else:
                from ml.concrete_pretrained import ConcretePretrainedClientModel
                model = ConcretePretrainedClientModel(models_dir, model_name=args.model)
        except Exception as e:
            logger.error(f"Lỗi khởi tạo mô hình Concrete: {e}")
            sys.exit(1)
    else:
        logger.error(f"Nền tảng {platform} chưa được hỗ trợ.")
        sys.exit(1)
            
    print(f"Mô hình đã nạp: {args.model} | Nền tảng: {platform.upper()}")
    print(model.get_prompt_info())
    
    text = input("\nNhập dữ liệu (văn bản) cần phân loại: ")
    if not text.strip():
        text = "I love learning about artificial intelligence and space exploration."
        print(f"Mặc định sử dụng: '{text}'")
        
    client_payload = model.prepare_input(text)
        
    if platform == "openfhe":
        pin = getpass.getpass("Nhập mã PIN của bạn (để giải mã kết quả): ")
        
        # Lưu vector ra file tạm cho fhe_worker
        client_input_path = os.path.join(tmp_dir, "client_input.json")
        with open(client_input_path, 'w', encoding='utf-8') as f:
            json.dump({"vector": client_payload}, f)
            
        logger.info("Gửi dữ liệu sang FHE Server để tính toán ẩn danh (OpenFHE CKKS)...")
        if sys.platform == 'linux':
            python_executable = sys.executable
        else:
            python_executable = r"C:\msys64\mingw64\bin\python.exe"
            
        worker_script = os.path.join(base_dir, "core", "fhe_worker.py")
        worker_args = [python_executable, worker_script, "--pin", pin, "--model", args.model]
        
    elif platform == "concrete_ml":
        # Concrete ML lưu binary thay vì json
        enc_data_path = os.path.join(tmp_dir, "concrete_enc_data.bin")
        eval_keys_path = os.path.join(tmp_dir, "concrete_eval_keys.bin")
        
        with open(enc_data_path, 'wb') as f:
            f.write(client_payload["concrete_enc_data"])
        with open(eval_keys_path, 'wb') as f:
            f.write(client_payload["concrete_eval_keys"])
            
        logger.info("Gửi dữ liệu sang FHE Server để tính toán ẩn danh (Concrete ML TFHE)...")
        python_executable = sys.executable
        worker_script = os.path.join(base_dir, "core", "concrete_worker.py")
        worker_args = [python_executable, worker_script, "--model", args.model]

    try:
        subprocess.run(worker_args, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Worker bị lỗi: {e}")
        sys.exit(1)
        
    if platform == "openfhe":
        result_path = os.path.join(tmp_dir, "result.json")
        if not os.path.exists(result_path):
            logger.error("Không nhận được kết quả từ FHE Worker.")
            sys.exit(1)
            
        with open(result_path, 'r', encoding='utf-8') as f:
            result_data = json.load(f)
            
    elif platform == "concrete_ml":
        result_path = os.path.join(tmp_dir, "concrete_enc_result.bin")
        if not os.path.exists(result_path):
            logger.error("Không nhận được kết quả từ Concrete Worker.")
            sys.exit(1)
            
        with open(result_path, 'rb') as f:
            result_data = {"concrete_enc_result": f.read()}
            
    model.interpret_result(result_data)

if __name__ == "__main__":
    main()
