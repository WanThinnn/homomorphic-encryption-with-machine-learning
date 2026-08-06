import os
import json
import math
import logging

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:
    pass

logger = logging.getLogger(__name__)

class LogisticRegressionClientModel:
    def __init__(self, models_dir):
        self.vocab = []
        self.categories = []
        self.idf = []
        
        vocab_path = os.path.join(models_dir, "vocab.json")
        weights_path = os.path.join(models_dir, "weights.json")
        
        if not os.path.exists(vocab_path) or not os.path.exists(weights_path):
            raise FileNotFoundError("Không tìm thấy model thật. Hãy chạy src/ml/download_model.py trước.")
            
        with open(vocab_path, 'r', encoding='utf-8') as f:
            vocab_data = json.load(f)
            self.vocab = vocab_data['vocabulary']
            self.idf = vocab_data['idf']
            
        with open(weights_path, 'r', encoding='utf-8') as f:
            weight_data = json.load(f)
            self.categories = weight_data['categories']
            
    def get_prompt_info(self):
        return f"Phân loại giữa [{self.categories[0]}] và [{self.categories[1]}]"

    def prepare_input(self, text):
        logger.info("Đang Vector hóa văn bản (TF-IDF)...")
        vectorizer = TfidfVectorizer(vocabulary=self.vocab, stop_words='english')
        # Hack để bypass việc fit
        vectorizer.fit(["dummy"]) 
        vectorizer.idf_ = self.idf
        
        # Chuyển đổi văn bản thành vector
        vector = vectorizer.transform([text]).toarray()[0].tolist()
        return vector

    def interpret_result(self, raw_result):
        # Result from server is a dict with 'logit'
        logit = raw_result.get('logit', 0.0)
        
        def sigmoid(x):
            if x < -709: return 0.0
            if x > 709: return 1.0
            return 1 / (1 + math.exp(-x))
            
        prob = sigmoid(logit)
        
        print("\n============================================================")
        print(" KẾT QUẢ DỰ ĐOÁN (SAU KHI GIẢI MÃ TỪ FHE)")
        print("============================================================")
        print(f"Logit thô (FHE trả về) : {logit:.4f}")
        print(f"Xác suất thuộc lớp [{self.categories[1]}] : {prob * 100:.2f}%")
        print(f"Xác suất thuộc lớp [{self.categories[0]}] : {(1 - prob) * 100:.2f}%")
        
        if prob > 0.5:
            print(f"\n=> KẾT LUẬN: Văn bản thuộc chủ đề: {self.categories[1].upper()}!")
        else:
            print(f"\n=> KẾT LUẬN: Văn bản thuộc chủ đề: {self.categories[0].upper()}!")
