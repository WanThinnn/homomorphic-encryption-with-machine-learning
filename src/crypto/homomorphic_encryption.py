import logging
from typing import List, Any
import os
import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger(__name__)

try:
    import openfhe
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
        self.public_key = None
        self.private_key = None
        
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
            # Bật tính năng Advanced SHE (cho các phép tính phức tạp như EvalSum)
            self.crypto_context.Enable(PKESchemeFeature.ADVANCEDSHE)
            
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
        kp = self.crypto_context.KeyGen()
        self.public_key = kp.publicKey
        self.private_key = kp.secretKey
        logger.info("Đang tạo Khóa Relinearization (EvalMultKey) cho phép nhân...")
        self.crypto_context.EvalMultKeyGen(self.private_key)
        
        logger.info("Đang tạo Khóa Rotation (EvalSumKey) cho phép tính tổng vector...")
        try:
            self.crypto_context.EvalSumKeyGen(self.private_key)
        except Exception as e:
            logger.warning(f"Lỗi khi tạo EvalSumKey: {e}. Bạn có thể bỏ qua nếu không dùng EvalSum.")
            
        return kp
        
    def _derive_key(self, pin: str, salt: bytes) -> bytes:
        """Sử dụng PBKDF2HMAC để dẫn xuất khóa 256-bit từ mã PIN."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600000,
            backend=default_backend()
        )
        return kdf.derive(pin.encode('utf-8'))
        
    def save_keys(self, pin: str, secrets_dir: str = "secrets"):
        """Lưu khóa công khai, ngữ cảnh và khóa bí mật (được mã hóa AES-GCM) vào đĩa."""
        if not OPENFHE_LOADED:
            logger.warning("Mock: Bỏ qua việc lưu khóa.")
            return
            
        os.makedirs(secrets_dir, exist_ok=True)
        
        # Lưu CryptoContext
        cc_path = os.path.join(secrets_dir, "cryptocontext.bin")
        openfhe.SerializeToFile(cc_path, self.crypto_context, openfhe.BINARY)
        
        # Lưu Public Key
        pub_path = os.path.join(secrets_dir, "public_key.bin")
        openfhe.SerializeToFile(pub_path, self.public_key, openfhe.BINARY)
        
        # Lưu Eval Keys
        mult_key_path = os.path.join(secrets_dir, "eval_mult_key.bin")
        self.crypto_context.SerializeEvalMultKey(mult_key_path, openfhe.BINARY, "")
        
        sum_key_path = os.path.join(secrets_dir, "eval_sum_key.bin")
        self.crypto_context.SerializeEvalAutomorphismKey(sum_key_path, openfhe.BINARY, "")
        
        # Serialize Private Key thẳng vào RAM (dạng bytes)
        priv_data = openfhe.Serialize(self.private_key, openfhe.BINARY)
        
        salt = os.urandom(16)
        aes_key = self._derive_key(pin, salt)
        nonce = os.urandom(12)
        
        aesgcm = AESGCM(aes_key)
        ciphertext = aesgcm.encrypt(nonce, priv_data, None)
        
        priv_enc_path = os.path.join(secrets_dir, "private_key.enc")
        with open(priv_enc_path, 'wb') as f:
            f.write(salt + nonce + ciphertext)
            
        logger.info(f"Đã lưu thành công và mã hóa Private Key (in-memory) vào {secrets_dir}/")

    def load_keys(self, pin: str, secrets_dir: str = "secrets") -> bool:
        """Tải khóa từ đĩa, giải mã Private Key bằng AES-GCM."""
        if not OPENFHE_LOADED:
            logger.warning("Mock: Bỏ qua việc tải khóa.")
            return False
            
        priv_enc_path = os.path.join(secrets_dir, "private_key.enc")
        if not os.path.exists(priv_enc_path):
            logger.error("Không tìm thấy Private Key.")
            return False
            
        # Giải mã Private Key
        try:
            with open(priv_enc_path, 'rb') as f:
                data = f.read()
            
            salt = data[:16]
            nonce = data[16:28]
            ciphertext = data[28:]
            
            aes_key = self._derive_key(pin, salt)
            aesgcm = AESGCM(aes_key)
            priv_data = aesgcm.decrypt(nonce, ciphertext, None)
            
            # Đọc lại bằng OpenFHE (Deserialize)
            # Do Python wrapper của OpenFHE trả về tuple(Object, bool)
            cc, ok1 = openfhe.DeserializeCryptoContext(os.path.join(secrets_dir, "cryptocontext.bin"), openfhe.BINARY)
            pub, ok2 = openfhe.DeserializePublicKey(os.path.join(secrets_dir, "public_key.bin"), openfhe.BINARY)
            
            # Load Private Key trực tiếp từ RAM
            priv = openfhe.DeserializePrivateKeyString(priv_data, openfhe.BINARY)
            
            if not (ok1 and ok2 and priv):
                raise Exception("Deserialize object failed")
                
            self.crypto_context = cc
            self.public_key = pub
            self.private_key = priv
            
            # Load Eval Keys
            mult_key_path = os.path.join(secrets_dir, "eval_mult_key.bin")
            if os.path.exists(mult_key_path):
                self.crypto_context.DeserializeEvalMultKey(mult_key_path, openfhe.BINARY)
                
            sum_key_path = os.path.join(secrets_dir, "eval_sum_key.bin")
            if os.path.exists(sum_key_path):
                self.crypto_context.DeserializeEvalAutomorphismKey(sum_key_path, openfhe.BINARY)
            
            logger.info("Đã giải mã và nạp Private Key (từ RAM) thành công!")
            return True
        except Exception as e:
            logger.error(f"Giải mã thất bại (Sai mã PIN, dữ liệu hỏng, hoặc format cũ): {e}")
            raise ValueError("Sai mã PIN hoặc dữ liệu khóa bị hỏng!")

    def encrypt_vector(self, vector: List[float]) -> Any:
        """
        Mã hóa một vector số thực (ví dụ 256D) thành Ciphertext.
        """
        if not OPENFHE_LOADED:
            logger.warning(f"Mock: Đang mã hóa vector độ dài {len(vector)}")
            return "mock_ciphertext"

        if not self.crypto_context or not self.public_key:
            raise ValueError("CryptoContext hoặc Khóa bị thiếu. Hãy gọi generate_keys() trước.")
            
        if len(vector) != self.vector_dim:
            logger.warning(f"Cảnh báo: Kích thước vector ({len(vector)}) khác với dự kiến ({self.vector_dim}).")

        # Nén vector thành dạng Plaintext tương thích CKKS
        plaintext = self.crypto_context.MakeCKKSPackedPlaintext(vector)
        # Mã hóa bằng Public Key
        return self.crypto_context.Encrypt(self.public_key, plaintext)

    def decrypt_vector(self, ciphertext: Any) -> List[float]:
        """
        Giải mã Ciphertext trở lại thành vector số thực bằng Private Key.
        """
        if not OPENFHE_LOADED:
            logger.warning("Mock: Đang giải mã ciphertext")
            return [0.0] * self.vector_dim

        if not self.crypto_context or not self.private_key:
            raise ValueError("CryptoContext hoặc Khóa bị thiếu.")
            
        # Giải mã bằng Private Key
        plaintext_result = self.crypto_context.Decrypt(ciphertext, self.private_key)
        
        # Chỉ lấy đúng số chiều cần thiết, loại bỏ các zero padding
        plaintext_result.SetLength(self.vector_dim)
        
        return plaintext_result.GetRealPackedValue()

    def encode_vector(self, vector: List[float]) -> Any:
        """Mã hóa vector thành dạng Plaintext (để nhân/cộng với Ciphertext)."""
        if not OPENFHE_LOADED:
            return "mock_plaintext"
        if len(vector) != self.vector_dim:
            logger.warning(f"Cảnh báo: Kích thước vector ({len(vector)}) khác với dự kiến ({self.vector_dim}).")
        return self.crypto_context.MakeCKKSPackedPlaintext(vector)

    def eval_add(self, ct1: Any, ct2: Any) -> Any:
        """Cộng hai Ciphertext, hoặc cộng Ciphertext với Plaintext."""
        if not OPENFHE_LOADED:
            return "mock_eval_add"
        return self.crypto_context.EvalAdd(ct1, ct2)

    def eval_mult(self, ct: Any, item: Any) -> Any:
        """Nhân Ciphertext với Ciphertext hoặc Plaintext."""
        if not OPENFHE_LOADED:
            return "mock_eval_mult"
        return self.crypto_context.EvalMult(ct, item)

    def eval_sum(self, ct: Any, batch_size: int = None) -> Any:
        """Tính tổng tất cả các phần tử trong Ciphertext."""
        if not OPENFHE_LOADED:
            return "mock_eval_sum"
        bs = batch_size if batch_size else self.batch_size
        if bs == 0:
            bs = self.vector_dim
        return self.crypto_context.EvalSum(ct, bs)
