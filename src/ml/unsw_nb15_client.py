"""
Client Model cho UNSW-NB15 Network Intrusion Detection với Concrete ML FHE.

Class này xử lý:
- Nạp model FHE đã compile từ thư mục deployment
- Tiền xử lý dữ liệu network flow (encoding, scaling) dựa trên metadata đã lưu
- Mã hóa (encrypt) dữ liệu input
- Giải mã (decrypt) và hiển thị kết quả phân loại
"""
import os
import sys
import json
import numpy as np
import logging

try:
    from concrete.ml.deployment import FHEModelClient
except ImportError:
    pass

logger = logging.getLogger(__name__)


class UNSWNB15ClientModel:
    """Client-side model cho Network Intrusion Detection trên dữ liệu đã mã hóa FHE."""

    # =========================================================================
    # Mô tả ngắn gọn các features chính trong UNSW-NB15
    # Dùng cho hiển thị và hướng dẫn người dùng
    # =========================================================================
    FEATURE_DESCRIPTIONS = {
        'source_port': 'Cổng nguồn (0-65535)',
        'destination_port': 'Cổng đích (0-65535)',
        'protocol': 'Giao thức mạng (TCP/UDP/ICMP/...)',
        'state': 'Trạng thái kết nối (FIN/CON/INT/...)',
        'dur': 'Thời gian kết nối (giây)',
        'sbytes': 'Bytes gửi từ nguồn',
        'dbytes': 'Bytes gửi từ đích',
        'sttl': 'TTL nguồn',
        'dttl': 'TTL đích',
        'sloss': 'Số packet mất từ nguồn',
        'dloss': 'Số packet mất từ đích',
        'service': 'Dịch vụ mạng (HTTP/FTP/DNS/...)',
        'sload': 'Tải nguồn (bits/sec)',
        'dload': 'Tải đích (bits/sec)',
        'spkts': 'Số packet nguồn',
        'dpkts': 'Số packet đích',
        'swin': 'Window size nguồn',
        'dwin': 'Window size đích',
        'stcpb': 'TCP base sequence number nguồn',
        'dtcpb': 'TCP base sequence number đích',
        'smeansz': 'Kích thước trung bình packet nguồn',
        'dmeansz': 'Kích thước trung bình packet đích',
        'trans_depth': 'Độ sâu transaction (HTTP)',
        'res_bdy_len': 'Kích thước body response',
        'sjit': 'Jitter nguồn',
        'djit': 'Jitter đích',
        'sintpkt': 'Thời gian trung bình giữa các packet nguồn',
        'dintpkt': 'Thời gian trung bình giữa các packet đích',
        'tcprtt': 'TCP Round Trip Time',
        'synack': 'Thời gian SYN-ACK',
        'ackdat': 'Thời gian ACK-DATA',
        'is_sm_ips_ports': 'Cùng IP và Port (0/1)',
        'ct_state_ttl': 'Số kết nối cùng state+TTL',
        'ct_flw_http_mthd': 'Số flow có HTTP method',
        'is_ftp_login': 'Có FTP login (0/1)',
        'ct_ftp_cmd': 'Số FTP command',
        'ct_srv_src': 'Số kết nối cùng service từ nguồn',
        'ct_srv_dst': 'Số kết nối cùng service đến đích',
        'ct_dst_ltm': 'Số kết nối đến đích (100 record gần nhất)',
        'ct_src_ltm': 'Số kết nối từ nguồn (100 record gần nhất)',
        'ct_src_dport_ltm': 'Số kết nối từ nguồn đến port đích',
        'ct_dst_sport_ltm': 'Số kết nối đến đích từ port nguồn',
        'ct_dst_src_ltm': 'Số kết nối giữa nguồn và đích',
    }

    def __init__(self, models_dir, model_name):
        self.deploy_dir = os.path.join(models_dir, model_name)
        self.key_dir = os.path.join(models_dir, "..", "..", "secrets", "concrete")
        os.makedirs(self.key_dir, exist_ok=True)

        # Kiểm tra model đã được compile chưa
        if not os.path.exists(os.path.join(self.deploy_dir, "client.zip")):
            raise FileNotFoundError(
                "Chưa tìm thấy mô hình UNSW-NB15 đã compile!\n"
                "Hãy chạy lệnh sau trên WSL/Linux trước:\n"
                "  python3 src/ml/train_unsw_nb15.py"
            )

        # Nạp preprocessing metadata
        metadata_path = os.path.join(self.deploy_dir, "preprocessing_metadata.json")
        if not os.path.exists(metadata_path):
            raise FileNotFoundError(
                "Không tìm thấy preprocessing_metadata.json!\n"
                "Hãy chạy lại: python3 src/ml/train_unsw_nb15.py"
            )

        with open(metadata_path, 'r', encoding='utf-8') as f:
            self.metadata = json.load(f)

        self.feature_names = self.metadata['feature_names']
        self.categorical_cols = self.metadata['categorical_cols']
        self.label_encoders = self.metadata['label_encoders']
        self.scaler_mean = np.array(self.metadata['scaler_mean'], dtype=np.float32)
        self.scaler_scale = np.array(self.metadata['scaler_scale'], dtype=np.float32)
        self.target_names = self.metadata['target_names']

        # Nạp sample inputs (nếu có) để demo
        samples_path = os.path.join(self.deploy_dir, "sample_inputs.json")
        self.sample_data = None
        if os.path.exists(samples_path):
            with open(samples_path, 'r', encoding='utf-8') as f:
                self.sample_data = json.load(f)

        # Khởi tạo FHE Client
        self.client = FHEModelClient(self.deploy_dir, key_dir=self.key_dir)

        # Sinh khóa FHE
        logger.info("Đang nạp/tạo FHE Keys cho Concrete ML (UNSW-NB15)...")
        self.client.generate_private_and_evaluation_keys()

    def get_prompt_info(self):
        """Trả về thông tin mô hình để hiển thị."""
        info = (
            f"\n{'='*60}\n"
            f" 🛡️  NETWORK INTRUSION DETECTION (UNSW-NB15)\n"
            f"{'='*60}\n"
            f" Dataset    : UNSW-NB15 (Hugging Face: rdpahalavan/UNSW-NB15)\n"
            f" Bài toán   : Binary Classification (Normal vs Attack)\n"
            f" Mô hình    : XGBoost ({self.metadata['model_params']['n_estimators']} trees, "
            f"depth={self.metadata['model_params']['max_depth']})\n"
            f" Features   : {self.metadata['n_features']} features (đủ 49 features gốc)\n"
            f" Accuracy   : {self.metadata['accuracy_cleartext']*100:.2f}% (cleartext)\n"
            f" FHE Backend: Concrete ML (TFHE - Lượng tử hóa {self.metadata['model_params']['n_bits']}-bit)\n"
            f"{'='*60}\n"
        )

        if self.sample_data:
            info += (
                f"\n Có {len(self.sample_data['samples'])} mẫu test sẵn.\n"
                f" Nhập 'sample' hoặc số thứ tự (1-{len(self.sample_data['samples'])}) để dùng mẫu có sẵn.\n"
                f" Hoặc nhập 'random' để tạo network flow ngẫu nhiên.\n"
            )

        return info

    def prepare_input(self, text):
        """
        Chuẩn bị và mã hóa dữ liệu input.

        Hỗ trợ:
        - 'sample' hoặc 'sample N': Dùng mẫu test có sẵn
        - 'random': Tạo random network flow
        - Nhập trực tiếp: Chuỗi các giá trị cách nhau bởi dấu phẩy
        """
        text = text.strip().lower()

        if text.startswith('sample') and self.sample_data:
            # Dùng mẫu có sẵn
            parts = text.split()
            if len(parts) > 1 and parts[1].isdigit():
                idx = int(parts[1]) - 1
            else:
                idx = 0

            idx = max(0, min(idx, len(self.sample_data['samples']) - 1))
            input_vector = np.array(
                [self.sample_data['samples'][idx]], dtype=np.float32
            )
            true_label = self.sample_data['labels'][idx]
            label_name = "Normal" if true_label == 0 else "Attack"
            logger.info(f"Sử dụng mẫu test #{idx+1} — Nhãn thực: {label_name} (label={true_label})")
            logger.info(f"  Mô tả: {self.sample_data['descriptions'][idx]}")

        elif text == 'random':
            # Tạo random network flow
            logger.info("Tạo network flow ngẫu nhiên để test...")
            np.random.seed(None)  # Truly random
            input_vector = np.random.randn(1, len(self.feature_names)).astype(np.float32)

        else:
            # Parse input trực tiếp (dạng CSV: giá trị cách nhau bởi dấu phẩy)
            try:
                values = [float(v.strip()) for v in text.split(',')]
                if len(values) != len(self.feature_names):
                    logger.warning(
                        f"Số features nhập ({len(values)}) khác với yêu cầu ({len(self.feature_names)}). "
                        f"Sử dụng mẫu mặc định thay thế."
                    )
                    # Fallback: dùng sample đầu tiên
                    if self.sample_data:
                        input_vector = np.array(
                            [self.sample_data['samples'][0]], dtype=np.float32
                        )
                        logger.info("Sử dụng mẫu test mặc định #1")
                    else:
                        input_vector = np.zeros((1, len(self.feature_names)), dtype=np.float32)
                else:
                    input_vector = np.array([values], dtype=np.float32)
                    # Chuẩn hóa bằng scaler đã lưu
                    input_vector = (input_vector - self.scaler_mean) / self.scaler_scale
                    input_vector = input_vector.astype(np.float32)
            except ValueError:
                logger.warning("Không thể parse input. Sử dụng mẫu test mặc định.")
                if self.sample_data:
                    input_vector = np.array(
                        [self.sample_data['samples'][0]], dtype=np.float32
                    )
                else:
                    input_vector = np.zeros((1, len(self.feature_names)), dtype=np.float32)

        logger.info(f"Vector input shape: {input_vector.shape}")
        logger.info("Mã hóa đầu vào với khóa bảo mật (Quantize + Encrypt + Serialize)...")

        # Quantize, Encrypt và Serialize thành bytes
        encrypted_data = self.client.quantize_encrypt_serialize(input_vector)
        serialized_evaluation_keys = self.client.get_serialized_evaluation_keys()

        return {
            "concrete_enc_data": encrypted_data,
            "concrete_eval_keys": serialized_evaluation_keys
        }

    def interpret_result(self, result_data):
        """Giải mã và hiển thị kết quả phân loại từ FHE Server."""
        logger.info("Đang giải mã kết quả từ FHE Server...")

        if "concrete_enc_result" not in result_data:
            logger.error("Không tìm thấy kết quả hợp lệ!")
            return

        enc_result = result_data["concrete_enc_result"]

        # Giải mã và Dequantize
        decrypted_prediction = self.client.deserialize_decrypt_dequantize(enc_result)

        print("")
        print("=" * 60)
        print(" 🛡️  KẾT QUẢ PHÁT HIỆN XÂM NHẬP MẠNG (FHE - Encrypted)")
        print("=" * 60)

        # XGBClassifier trả về xác suất cho mỗi class
        raw_output = decrypted_prediction[0]
        print(f" Xác suất thô (sau giải mã): {raw_output}")

        if len(raw_output) >= 2:
            prob_normal = raw_output[0]
            prob_attack = raw_output[1]
            pred_class = np.argmax(raw_output)
        else:
            # Trường hợp output là scalar
            pred_class = int(raw_output[0] > 0.5) if len(raw_output) == 1 else 0
            prob_normal = 1 - raw_output[0] if len(raw_output) == 1 else 0
            prob_attack = raw_output[0] if len(raw_output) == 1 else 0

        print(f" Xác suất Normal : {prob_normal:.4f}")
        print(f" Xác suất Attack : {prob_attack:.4f}")
        print("")

        if pred_class == 0:
            print(" ✅ KẾT LUẬN: TRAFFIC BÌNH THƯỜNG (Normal)")
            print("    Không phát hiện dấu hiệu xâm nhập đáng ngờ.")
        else:
            print(" 🚨 KẾT LUẬN: PHÁT HIỆN XÂM NHẬP (Attack Detected!)")
            print("    Cảnh báo: Traffic này có dấu hiệu tấn công mạng!")
            print("    Đề xuất: Kiểm tra chi tiết nguồn gốc và nội dung kết nối.")

        print("")
        print(" ℹ️  Lưu ý: Toàn bộ quá trình inference được thực hiện trên")
        print("    dữ liệu đã mã hóa (FHE). Server KHÔNG biết nội dung")
        print("    input hay kết quả — chỉ Client mới có thể giải mã.")
        print("=" * 60)
