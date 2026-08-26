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
        self._eval_keys = None

        logger.info("Đang nạp/tạo FHE Keys cho Concrete ML (UNSW-NB15)...")
        try:
            self.client.generate_private_and_evaluation_keys(force=False)
        except TypeError:
            self.client.generate_private_and_evaluation_keys()

    def _get_eval_keys(self):
        if self._eval_keys is None:
            self._eval_keys = self.client.get_serialized_evaluation_keys()
        return self._eval_keys

    def _encrypt_vectors(self, input_vectors):
        payloads = []
        total = len(input_vectors)
        for i in range(total):
            if total > 1:
                logger.info("Mã hóa mẫu %d/%d (Quantize + Encrypt + Serialize)...", i + 1, total)
            payloads.append(self.client.quantize_encrypt_serialize(input_vectors[i:i + 1]))
        return {
            "concrete_enc_data": payloads,
            "concrete_eval_keys": self._get_eval_keys(),
        }

    def _features_to_vector(self, parsed_features):
        parsed = dict(parsed_features)
        for col in self.categorical_cols:
            val = str(parsed.get(col, '')).lower()
            if col in self.label_encoders:
                classes = self.label_encoders[col]['classes']
                if val in classes:
                    parsed[col] = classes.index(val)
                else:
                    parsed[col] = classes.index('unknown') if 'unknown' in classes else 0
            else:
                parsed[col] = 0

        values = [parsed.get(col, 0.0) for col in self.feature_names]
        input_vector = np.array([values], dtype=np.float32)
        input_vector = (input_vector - self.scaler_mean) / self.scaler_scale
        return input_vector.astype(np.float32)

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
        return self._encrypt_vectors(input_vector)

    def prepare_suricata_input(self, parsed_features):
        """Mã hóa 1 record Suricata (giữ tương thích)."""
        return self.prepare_suricata_inputs([parsed_features])

    def prepare_suricata_inputs(self, parsed_features_list):
        """Mã hóa nhiều record Suricata; eval keys chỉ serialize 1 lần."""
        vectors = [self._features_to_vector(feat) for feat in parsed_features_list]
        input_vectors = np.vstack(vectors)
        logger.info("Mã hóa %d record Suricata (eval keys reuse)...", len(input_vectors))
        return self._encrypt_vectors(input_vectors)

    def _decode_prediction(self, enc_result):
        decrypted_prediction = self.client.deserialize_decrypt_dequantize(enc_result)
        raw_output = decrypted_prediction[0]
        if len(raw_output) >= 2:
            pred_class = int(np.argmax(raw_output))
            prob_normal = float(raw_output[0])
            prob_attack = float(raw_output[1])
        else:
            pred_class = int(raw_output[0] > 0.5) if len(raw_output) == 1 else 0
            prob_normal = float(1 - raw_output[0]) if len(raw_output) == 1 else 0.0
            prob_attack = float(raw_output[0]) if len(raw_output) == 1 else 0.0
        return pred_class, prob_normal, prob_attack, raw_output

    def interpret_result(self, result_data, batch_meta=None):
        """Giải mã và hiển thị kết quả (1 mẫu hoặc batch)."""
        enc_results = result_data.get("concrete_enc_results")
        if enc_results is None and "concrete_enc_result" in result_data:
            enc_results = [result_data["concrete_enc_result"]]
        if not enc_results:
            logger.error("Không tìm thấy kết quả hợp lệ!")
            return

        logger.info("Đang giải mã %d kết quả từ FHE Server...", len(enc_results))
        decoded = [self._decode_prediction(blob) for blob in enc_results]
        attack_count = sum(1 for pred, *_ in decoded if pred == 1)

        print("")
        print("=" * 60)
        print(" 🛡️  KẾT QUẢ PHÁT HIỆN XÂM NHẬP MẠNG (FHE - Encrypted)")
        print("=" * 60)
        print(f" Số mẫu      : {len(decoded)}")
        print(f" Normal      : {len(decoded) - attack_count}")
        print(f" Attack      : {attack_count}")
        print("-" * 60)

        for idx, (pred_class, prob_normal, prob_attack, raw_output) in enumerate(decoded, start=1):
            meta = {}
            if batch_meta and idx - 1 < len(batch_meta):
                meta = batch_meta[idx - 1]
            src = meta.get("src_ip", "?")
            dst = meta.get("dest_ip", "?")
            event_type = meta.get("event_type", "?")
            label = "ATTACK" if pred_class == 1 else "NORMAL"
            print(
                f" [{idx:03d}] {label:6s}  N={prob_normal:.4f} A={prob_attack:.4f}"
                f"  {src} -> {dst}  ({event_type})"
            )
            if len(decoded) == 1:
                print(f"       Xác suất thô: {raw_output}")

        print("")
        print(" ℹ️  Inference chạy trên ciphertext. Server không thấy input/kết quả.")
        print("=" * 60)
