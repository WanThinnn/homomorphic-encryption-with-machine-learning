import os
import sys
import json
import math
import getpass
import subprocess
import logging

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:
    print("Vui lòng cài đặt scikit-learn trên Python gốc.")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - CLIENT - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def sigmoid(x):
    # Tránh overflow
    if x < -709:
        return 0.0
    if x > 709:
        return 1.0
    return 1 / (1 + math.exp(-x))

def main():
    print("============================================================")
    print("     PHÂN LOẠI CHỦ ĐỀ VĂN BẢN VỚI OPENFHE                   ")
    print("      (Mô hình: Logistic Regression + TF-IDF)               ")
    print("============================================================")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, "ml", "models")
    tmp_dir = os.path.join(base_dir, "..", "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    
    # 1. Nạp Vocab và Categories
    vocab_path = os.path.join(models_dir, "vocab.json")
    weights_path = os.path.join(models_dir, "weights.json")
    if not os.path.exists(vocab_path) or not os.path.exists(weights_path):
        print("Lỗi: Không tìm thấy model thật. Hãy chạy src/ml/download_model.py trước.")
        sys.exit(1)
        
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab_data = json.load(f)
        vocab = vocab_data['vocabulary']
        
    with open(weights_path, 'r', encoding='utf-8') as f:
        weight_data = json.load(f)
        categories = weight_data['categories']
        
    print(f"Mô hình đã nạp sẵn: Phân loại giữa [{categories[0]}] và [{categories[1]}]")
    text = input("\nNhập văn bản tiếng Anh cần phân loại: ")
    if not text.strip():
        text = "I love learning about artificial intelligence and space exploration."
        print(f"Mặc định sử dụng: '{text}'")
        
    pin = getpass.getpass("Nhập mã PIN của bạn (để giải mã kết quả): ")
    
    # 2. Vector hóa văn bản bằng System Python (Tfidf)
    logger.info("Đang Vector hóa văn bản (TF-IDF)...")
    vectorizer = TfidfVectorizer(vocabulary=vocab, stop_words='english')
    # Hack để bypass việc fit
    vectorizer.fit(["dummy"]) 
    vectorizer.idf_ = vocab_data['idf']
    
    # Chuyển đổi văn bản thành vector (256 chiều)
    vector = vectorizer.transform([text]).toarray()[0].tolist()
    
    # Lưu ra file tạm cho fhe_worker
    client_input_path = os.path.join(tmp_dir, "client_input.json")
    with open(client_input_path, 'w', encoding='utf-8') as f:
        json.dump({"vector": vector}, f)
        
    # 3. Gọi FHE Worker (MinGW Python) để xử lý mã hóa
    logger.info("Gửi dữ liệu sang FHE Server để tính toán ẩn danh...")
    
    mingw_python = r"C:\msys64\mingw64\bin\python.exe"
    worker_script = os.path.join(base_dir, "core", "fhe_worker.py")
    
    try:
        subprocess.run([mingw_python, worker_script, pin], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"FHE Worker bị lỗi: {e}")
        sys.exit(1)
        
    # 4. Đọc kết quả giải mã và tính xác suất
    result_path = os.path.join(tmp_dir, "result.json")
    if not os.path.exists(result_path):
        logger.error("Không nhận được kết quả từ FHE Worker.")
        sys.exit(1)
        
    with open(result_path, 'r', encoding='utf-8') as f:
        result_data = json.load(f)
        logit = result_data['logit']
        
    prob = sigmoid(logit)
    
    print("\n============================================================")
    print(" KẾT QUẢ DỰ ĐOÁN (SAU KHI GIẢI MÃ TỪ FHE)")
    print("============================================================")
    print(f"Logit thô (FHE trả về) : {logit:.4f}")
    print(f"Xác suất thuộc lớp [{categories[1]}] : {prob * 100:.2f}%")
    print(f"Xác suất thuộc lớp [{categories[0]}] : {(1 - prob) * 100:.2f}%")
    
    if prob > 0.5:
        print(f"\n=> KẾT LUẬN: Văn bản thuộc chủ đề: {categories[1].upper()}!")
    else:
        print(f"\n=> KẾT LUẬN: Văn bản thuộc chủ đề: {categories[0].upper()}!")

if __name__ == "__main__":
    main()
