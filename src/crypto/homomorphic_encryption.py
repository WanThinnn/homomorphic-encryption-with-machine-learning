import logging
from typing import List, Any
import os
import secrets
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Random import get_random_bytes

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
        self.key_pair = self.crypto_context.KeyGen()
        
        logger.info("Đang tạo Khóa Relinearization (EvalMultKey) cho phép nhân...")
        self.crypto_context.EvalMultKeyGen(self.key_pair.secretKey)
        
        logger.info("Đang tạo Khóa Rotation (EvalSumKey) cho phép tính tổng vector...")
        try:
            self.crypto_context.EvalSumKeyGen(self.key_pair.secretKey)
        except Exception as e:
            logger.warning(f"Lỗi khi tạo EvalSumKey: {e}. Bạn có thể bỏ qua nếu không dùng EvalSum.")
            
        return self.key_pair
        
    def _derive_key(self, pin: str, salt: bytes) -> bytes:
        """Sử dụng PBKDF2HMAC để dẫn xuất khóa 256-bit từ mã PIN."""
        return PBKDF2(pin.encode('utf-8'), salt, dkLen=32, count=600000)
        
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
        openfhe.SerializeToFile(pub_path, self.key_pair.publicKey, openfhe.BINARY)
        
        # Lưu Private Key (tạm thời)
        priv_temp_path = os.path.join(secrets_dir, "private_key.tmp")
        openfhe.SerializeToFile(priv_temp_path, self.key_pair.secretKey, openfhe.BINARY)
        
        # Mã hóa Private Key bằng AES-GCM-256
        with open(priv_temp_path, 'rb') as f:
            priv_data = f.read()
            
        salt = get_random_bytes(16)
        aes_key = self._derive_key(pin, salt)
        nonce = get_random_bytes(12)
        
        cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
        ciphertext, tag = cipher.encrypt_and_digest(priv_data)
        
        priv_enc_path = os.path.join(secrets_dir, "private_key.enc")
        with open(priv_enc_path, 'wb') as f:
            f.write(salt + nonce + tag + ciphertext)
            
        # Xóa file tạm
        os.remove(priv_temp_path)
        logger.info(f"Đã lưu thành công và mã hóa Private Key vào {secrets_dir}/")

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
            tag = data[28:44]
            ciphertext = data[44:]
            
            aes_key = self._derive_key(pin, salt)
            cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
            priv_data = cipher.decrypt_and_verify(ciphertext, tag)
            
            priv_temp_path = os.path.join(secrets_dir, "private_key_dec.tmp")
            with open(priv_temp_path, 'wb') as f:
                f.write(priv_data)
                
            # Đọc lại bằng OpenFHE (Deserialize)
            # Do Python wrapper của OpenFHE Deserialize có cách gọi deserialize khác nhau,
            # (ví dụ SerializeToFile -> DeserializeFromFile). 
            # Giả sử ta tái tạo lại hoặc OpenFHE tự động nạp.
            # Lưu ý: Hiện OpenFHE python binding có hàm DeserializeCryptoContext, DeserializePrivateKey...
            cc, pub, priv = openfhe.CryptoContext(), openfhe.PublicKey(), openfhe.PrivateKey()
            openfhe.DeserializeCryptoContext(os.path.join(secrets_dir, "cryptocontext.bin"), cc, openfhe.BINARY)
            openfhe.DeserializePublicKey(os.path.join(secrets_dir, "public_key.bin"), pub, openfhe.BINARY)
            openfhe.DeserializePrivateKey(priv_temp_path, priv, openfhe.BINARY)
            
            self.crypto_context = cc
            self.key_pair = openfhe.KeyPair(pub, priv)
            
            os.remove(priv_temp_path)
            logger.info("Đã giải mã và nạp Private Key thành công!")
            return True
        except ValueError as e:
            logger.error(f"Giải mã thất bại (Sai mã PIN hoặc dữ liệu bị hỏng): {e}")
            if os.path.exists(os.path.join(secrets_dir, "private_key_dec.tmp")):
                os.remove(os.path.join(secrets_dir, "private_key_dec.tmp"))
            return False

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
