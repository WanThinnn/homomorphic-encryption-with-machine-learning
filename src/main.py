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
    parser.add_argument("--model", type=str, required=True, help="Tên mô hình muốn chạy (vd: logistic_regression)")
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, "ml", "models")
    tmp_dir = os.path.join(base_dir, "..", "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    
    print("============================================================")
    print("     PHÂN LOẠI VỚI OPENFHE VÀ MACHINE LEARNING              ")
    print("============================================================")
    
    if args.model == "logistic_regression":
        try:
            from ml.logistic_regression import LogisticRegressionClientModel
            model = LogisticRegressionClientModel(models_dir)
        except Exception as e:
            logger.error(f"Lỗi khởi tạo mô hình: {e}")
            sys.exit(1)
            
        print(f"Mô hình đã nạp: {args.model}")
        print(model.get_prompt_info())
        
        text = input("\nNhập dữ liệu (văn bản) cần phân loại: ")
        if not text.strip():
            text = "I love learning about artificial intelligence and space exploration."
            print(f"Mặc định sử dụng: '{text}'")
            
        vector = model.prepare_input(text)
    else:
        logger.error(f"Mô hình {args.model} chưa được hỗ trợ.")
        sys.exit(1)
        
    pin = getpass.getpass("Nhập mã PIN của bạn (để giải mã kết quả): ")
    
    # Lưu vector ra file tạm cho fhe_worker
    client_input_path = os.path.join(tmp_dir, "client_input.json")
    with open(client_input_path, 'w', encoding='utf-8') as f:
        json.dump({"vector": vector}, f)
        
    logger.info("Gửi dữ liệu sang FHE Server để tính toán ẩn danh...")
    
    if sys.platform == 'linux':
        python_executable = sys.executable
    else:
        python_executable = r"C:\msys64\mingw64\bin\python.exe"
        
    worker_script = os.path.join(base_dir, "core", "fhe_worker.py")
    
    try:
        subprocess.run([python_executable, worker_script, pin], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"FHE Worker bị lỗi: {e}")
        sys.exit(1)
        
    result_path = os.path.join(tmp_dir, "result.json")
    if not os.path.exists(result_path):
        logger.error("Không nhận được kết quả từ FHE Worker.")
        sys.exit(1)
        
    with open(result_path, 'r', encoding='utf-8') as f:
        result_data = json.load(f)
        
    model.interpret_result(result_data)

if __name__ == "__main__":
    main()
