import logging
from typing import List, Any
import os

logger = logging.getLogger(__name__)

try:
    from openfhe import (
        CCParamsCKKSRNS,
        GenCryptoContext,
        PKESchemeFeature,
    )
    OPENFHE_LOADED = True
except ImportError:
    OPENFHE_LOADED = False


class FHEPipeline:
    """
    Quản lý luồng mã hóa, giải mã và tạo khóa bằng lược đồ CKKS (OpenFHE).
    Phục vụ cho việc mã hóa Graph Vector 256D trước khi gửi lên Cloud SOC.
    """

    def __init__(self, mult_depth: int = 5, scale_mod_size: int = 40, batch_size: int = 0, vector_dim: int = 256):
        self.mult_depth = mult_depth
        self.scale_mod_size = scale_mod_size
        self.batch_size = batch_size
        self.vector_dim = vector_dim
        
        self.crypto_context = None
        self.key_pair = None
        
        if OPENFHE_LOADED:
            self._init_context()
        else:
            logger.warning("FHEPipeline khởi tạo trong trạng thái MOCK (OpenFHE chưa được nạp).")

    def _init_context(self):
        try:
            parameters = CCParamsCKKSRNS()
            parameters.SetMultiplicativeDepth(self.mult_depth)
            parameters.SetScalingModSize(self.scale_mod_size)
            parameters.SetBatchSize(self.batch_size)
            
            self.crypto_context = GenCryptoContext(parameters)
            # Bật tính năng mã hóa công khai (Public Key Encryption)
            self.crypto_context.Enable(PKESchemeFeature.PKE)
            # Bật tính năng khóa chuyển đổi (Key Switching) cho EvalMult
            self.crypto_context.Enable(PKESchemeFeature.KEYSWITCH)
            # Bật tính năng Leveled SHE (Tính toán đồng cấu)
            self.crypto_context.Enable(PKESchemeFeature.LEVELEDSHE)
            
            logger.info(f"FHE CryptoContext (CKKS) khởi tạo thành công. MultDepth={self.mult_depth}, ScaleMod={self.scale_mod_size}")
        except Exception as e:
            logger.error(f"Lỗi khi khởi tạo CryptoContext: {e}")
            raise

    def generate_keys(self) -> Any:
        """
        Tạo Cặp khóa (Public, Private) và Khóa tính toán (EvalMultKey).
        Client sẽ giữ Private Key, gửi Public Key và EvalMultKey lên Cloud.
        """
        if not OPENFHE_LOADED:
            logger.warning("Mock: Đang gọi generate_keys()")
            return None

        if not self.crypto_context:
            raise ValueError("CryptoContext chưa được khởi tạo.")
            
        logger.info("Đang tạo cặp khóa Public / Private...")
        self.key_pair = self.crypto_context.KeyGen()
        
        logger.info("Đang tạo Khóa Relinearization (EvalMultKey) cho phép nhân...")
        self.crypto_context.EvalMultKeyGen(self.key_pair.secretKey)
        
        return self.key_pair

    def encrypt_vector(self, vector: List[float]) -> Any:
        """
        Mã hóa một vector số thực (ví dụ 256D) thành Ciphertext.
        """
        if not OPENFHE_LOADED:
            logger.warning(f"Mock: Đang mã hóa vector độ dài {len(vector)}")
            return "mock_ciphertext"

        if not self.crypto_context or not self.key_pair:
            raise ValueError("CryptoContext hoặc Khóa bị thiếu. Hãy gọi generate_keys() trước.")
            
        if len(vector) != self.vector_dim:
            logger.warning(f"Cảnh báo: Kích thước vector ({len(vector)}) khác với dự kiến ({self.vector_dim}).")

        # Nén vector thành dạng Plaintext tương thích CKKS
        plaintext = self.crypto_context.MakeCKKSPackedPlaintext(vector)
        # Mã hóa bằng Public Key
        ciphertext = self.crypto_context.Encrypt(self.key_pair.publicKey, plaintext)
        
        return ciphertext

    def decrypt_vector(self, ciphertext: Any) -> List[float]:
        """
        Giải mã Ciphertext trở lại thành vector số thực bằng Private Key.
        """
        if not OPENFHE_LOADED:
            logger.warning("Mock: Đang giải mã ciphertext")
            return [0.0] * self.vector_dim

        if not self.crypto_context or not self.key_pair:
            raise ValueError("CryptoContext hoặc Khóa bị thiếu.")
            
        # Giải mã bằng Private Key
        plaintext_result = self.crypto_context.Decrypt(ciphertext, self.key_pair.secretKey)
        
        # Chỉ lấy đúng số chiều cần thiết, loại bỏ các zero padding
        plaintext_result.SetLength(self.vector_dim)
        
        return plaintext_result.GetRealPackedValue()
