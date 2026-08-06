from typing import List, Any
import logging

logger = logging.getLogger(__name__)

class EncryptedLinearRegression:
    """
    Mô hình Linear Regression hoạt động trên dữ liệu đã được mã hóa bằng FHE.
    """
    def __init__(self, weights: List[float], bias: float):
        self.weights = weights
        self.bias = bias
        self.encoded_weights = None
        self.encoded_bias = None
        
        logger.info(f"Khởi tạo mô hình Linear Regression với {len(weights)} features.")

    def precompute(self, fhe_pipeline: Any):
        """
        Chuẩn bị trước các tham số mô hình thành định dạng Plaintext của FHE.
        Điều này giúp tối ưu thời gian Inference, server không phải mã hóa lại trọng số mỗi lần.
        """
        if not hasattr(fhe_pipeline, 'encode_vector'):
            logger.warning("FHEPipeline không hỗ trợ encode_vector, chạy ở chế độ mock?")
            return
            
        # Mã hóa trọng số
        self.encoded_weights = fhe_pipeline.encode_vector(self.weights)
        
        # Bias thường cộng vào kết quả sum, ta tạo vector có tất cả các chiều là bias 
        # (hoặc chỉ slot đầu tiên, tùy thuộc vào hàm EvalSum trả về kết quả ở slot nào, thường EvalSum copy tổng ra mọi slot)
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
        # 1. W * X
        mult_result = fhe_pipeline.eval_mult(encrypted_input, self.encoded_weights)
        
        logger.info("Đang tính toán: Sum(W * X)...")
        # 2. Sum(W * X)
        sum_result = fhe_pipeline.eval_sum(mult_result)
        
        logger.info("Đang tính toán: Sum + B...")
        # 3. Kết quả + Bias
        final_result = fhe_pipeline.eval_add(sum_result, self.encoded_bias)
        
        return final_result
