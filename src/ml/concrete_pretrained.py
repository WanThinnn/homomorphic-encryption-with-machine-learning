import os
import sys
import numpy as np
import logging

try:
    from concrete.ml.deployment import FHEModelClient
except ImportError:
    pass

logger = logging.getLogger(__name__)

class ConcretePretrainedClientModel:
    def __init__(self, models_dir, model_name):
        self.deploy_dir = os.path.join(models_dir, model_name)
        self.key_dir = os.path.join(models_dir, "..", "..", "secrets", "concrete")
        os.makedirs(self.key_dir, exist_ok=True)
        
        if not os.path.exists(os.path.join(self.deploy_dir, "client.zip")):
            raise FileNotFoundError("Chưa tìm thấy mô hình. Hãy chạy 'python3 src/ml/compile_pretrained.py' trước!")
            
        self.client = FHEModelClient(self.deploy_dir, key_dir=self.key_dir)
        self._eval_keys = None

        logger.info("Đang nạp/tạo FHE Keys cho Concrete ML...")
        try:
            self.client.generate_private_and_evaluation_keys(force=False)
        except TypeError:
            self.client.generate_private_and_evaluation_keys()

    def _get_eval_keys(self):
        if self._eval_keys is None:
            self._eval_keys = self.client.get_serialized_evaluation_keys()
        return self._eval_keys

    def get_prompt_info(self):
        return "Pre-trained XGBoost (Concrete ML / TFHE) - Dự đoán với dữ liệu mô phỏng 256 chiều."

    def prepare_input(self, text):
        logger.info("Mã hóa đầu vào với khóa bảo mật...")
        
        # Tạo dữ liệu giả lập 256-D để test mô hình XGBoost
        # Trong thực tế, bạn sẽ dùng TF-IDF vectorizer để chuyển 'text' thành mảng 256 chiều
        np.random.seed(hash(text) % (2**32))
        dummy_vector = np.random.randn(1, 256).astype(np.float32)
        
        # Quantize và Encrypt thành ciphertext
        encrypted_data = self.client.quantize_and_encrypt(dummy_vector)
        if not isinstance(encrypted_data, (bytes, bytearray)):
            encrypted_data = self.client.quantize_encrypt_serialize(dummy_vector)

        return {
            "concrete_enc_data": [encrypted_data],
            "concrete_eval_keys": self._get_eval_keys(),
        }

    def interpret_result(self, result_data, batch_meta=None):
        logger.info("Đang giải mã kết quả từ FHE Server...")
        enc_results = result_data.get("concrete_enc_results")
        if enc_results is None and "concrete_enc_result" in result_data:
            enc_results = [result_data["concrete_enc_result"]]
        if not enc_results:
            logger.error("Không tìm thấy kết quả hợp lệ!")
            return

        enc_result = enc_results[0]
        
        # Giải mã và Dequantize
        decrypted_prediction = self.client.deserialize_decrypt_dequantize(enc_result)
        
        print("\n============================================================")
        print(" KẾT QUẢ DỰ ĐOÁN TỪ CONCRETE ML (TFHE)")
        print("============================================================")
        # XGBClassifier trả về xác suất hoặc logit tùy cấu hình.
        # decrypted_prediction là một mảng Numpy.
        pred_class = np.argmax(decrypted_prediction[0])
        print(f"Xác suất thô: {decrypted_prediction[0]}")
        
        if pred_class == 1:
            print("\n=> KẾT LUẬN: Thuộc lớp 1 (Tích cực / Đúng)!")
        else:
            print("\n=> KẾT LUẬN: Thuộc lớp 0 (Tiêu cực / Sai)!")
