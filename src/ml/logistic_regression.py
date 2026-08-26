import os
import json
import math
import logging
from typing import List, Any
import numpy as np

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:
    pass

logger = logging.getLogger(__name__)

class LogisticRegressionClientModel:
    def __init__(self, models_dir, model_name):
        self.vocab = []
        self.categories = []
        self.idf = []
        
        vocab_path = os.path.join(models_dir, model_name, "vocab.json")
        weights_path = os.path.join(models_dir, model_name, "weights.json")
        
        if not os.path.exists(vocab_path) or not os.path.exists(weights_path):
            raise FileNotFoundError("Không tìm thấy model thật. Hãy chạy src/ml/models/simple_logistic_regression/download_model.py trước.")
            
        with open(vocab_path, 'r', encoding='utf-8') as f:
            vocab_data = json.load(f)
            self.vocab = vocab_data['vocabulary']
            self.idf = vocab_data['idf']
            
        with open(weights_path, 'r', encoding='utf-8') as f:
            weight_data = json.load(f)
            self.categories = weight_data['categories']

        self._vectorizer = TfidfVectorizer(vocabulary=self.vocab, stop_words='english')
        self._vectorizer.fit(["dummy"])
        self._vectorizer.idf_ = np.array(self.idf)
            
    def get_prompt_info(self):
        return f"Phân loại giữa [{self.categories[0]}] và [{self.categories[1]}]"

    def prepare_input(self, text):
        logger.info("Đang Vector hóa văn bản (TF-IDF)...")
        vector = self._vectorizer.transform([text]).toarray()[0].tolist()
        return vector

    def interpret_result(self, raw_result, batch_meta=None):
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


class LogisticRegressionServerModel:
    """
    Mô hình Logistic Regression hoạt động trên dữ liệu đã được mã hóa bằng FHE (Phía Server).
    Thực chất là phép toán Linear Regression (W*X + B), phần phi tuyến tính (Sigmoid/Argmax) được xử lý ở Client.
    """
    def __init__(self, weights: List[float], bias: float):
        self.weights = weights
        self.bias = bias
        self.encoded_weights = None
        self.encoded_bias = None
        
        logger.info(f"Khởi tạo mô hình Logistic Regression (Server) với {len(weights)} features.")

    def precompute(self, fhe_pipeline: Any):
        """
        Chuẩn bị trước các tham số mô hình thành định dạng Plaintext của FHE.
        """
        if not hasattr(fhe_pipeline, 'encode_vector'):
            logger.warning("FHEPipeline không hỗ trợ encode_vector, chạy ở chế độ mock?")
            return
            
        self.encoded_weights = fhe_pipeline.encode_vector(self.weights)
        bias_vector = [self.bias] * len(self.weights)
        self.encoded_bias = fhe_pipeline.encode_vector(bias_vector)
        logger.info("Đã pre-compute weights và bias sang định dạng Plaintext.")

    def predict_encrypted(self, encrypted_input: Any, fhe_pipeline: Any) -> Any:
        """
        Thực hiện dự đoán trực tiếp trên dữ liệu mã hóa (Ciphertext).
        Phép toán: Y = Sum(W * X) + B
        """
        if not self.encoded_weights or not self.encoded_bias:
            self.precompute(fhe_pipeline)
            
        logger.info("Đang tính toán: W * X (Element-wise multiplication)...")
        mult_result = fhe_pipeline.eval_mult(encrypted_input, self.encoded_weights)
        
        logger.info("Đang tính toán: Sum(W * X)...")
        sum_result = fhe_pipeline.eval_sum(mult_result)
        
        logger.info("Đang tính toán: Sum + B...")
        final_result = fhe_pipeline.eval_add(sum_result, self.encoded_bias)
        
        return final_result
