import os
import json
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def prepare_pretrained_model():
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    
    logger.info("Đang tạo bộ dữ liệu chủ đề (Y tế vs Công nghệ)...")
    
    # Tập dữ liệu siêu nhỏ gọn để không phải tải từ internet (tránh lỗi mạng)
    corpus = [
        "I have a headache and need to go to the hospital for some medicine",
        "The patient is recovering from surgery and taking pills",
        "Doctors recommend healthy diet and exercise for good health",
        "Cancer treatment involves chemotherapy and radiation",
        "I want to buy a new laptop with high speed CPU and lots of RAM",
        "The software update fixed a lot of bugs in the operating system",
        "Artificial intelligence and machine learning are the future of programming",
        "I need a good graphics card to play video games on my computer"
    ]
    # 0 = Y Tế (sci.med), 1 = Công nghệ (comp.graphics)
    y_train = [0, 0, 0, 0, 1, 1, 1, 1]
    target_names = ['sci.med (Y tế)', 'comp.graphics (Công nghệ)']
    
    logger.info("Đang tạo bộ từ vựng (TfidfVectorizer)...")
    # Tối đa 128 từ để FHE chạy nhanh
    vectorizer = TfidfVectorizer(max_features=128, stop_words='english')
    X_train = vectorizer.fit_transform(corpus)
    
    logger.info("Đang huấn luyện mô hình Logistic Regression...")
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)
    
    # Lấy trọng số
    weights = clf.coef_[0].tolist()
    bias = clf.intercept_[0]
    vocab = {k: int(v) for k, v in vectorizer.vocabulary_.items()}
    idf = vectorizer.idf_.tolist()
    
    # Lưu ra JSON cho FHE Server
    weights_path = os.path.join(models_dir, "weights.json")
    with open(weights_path, 'w', encoding='utf-8') as f:
        json.dump({"weights": weights, "bias": bias, "categories": target_names}, f, indent=4)
        
    vocab_path = os.path.join(models_dir, "vocab.json")
    with open(vocab_path, 'w', encoding='utf-8') as f:
        json.dump({"vocabulary": vocab, "idf": idf}, f, indent=4)
        
    logger.info(f"Hoàn tất! Đã lưu Weights ({len(weights)} chiều) và Vocab vào thư mục: {models_dir}")

if __name__ == "__main__":
    prepare_pretrained_model()
