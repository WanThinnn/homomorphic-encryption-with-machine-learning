"""
Train & Compile XGBoost trên UNSW-NB15 (Binary Classification) cho Concrete ML FHE.

Script này:
1. Download dataset UNSW-NB15 từ Hugging Face (rdpahalavan/UNSW-NB15)
2. Tiền xử lý: Label Encoding cho cột categorical, chuẩn hóa features
3. Train XGBoost bằng concrete.ml.sklearn.XGBClassifier
4. Compile mô hình sang mạch FHE (TFHE)
5. Lưu deployment artifacts (client.zip, server.zip) vào thư mục models/unsw_nb15_xgb/
6. Lưu preprocessing metadata (encoders, scaler, feature names) để Client có thể tái sử dụng

Yêu cầu: Chạy trên Linux/WSL với concrete-ml đã cài đặt.
    pip install concrete-ml datasets scikit-learn
"""
import os
import sys
import json
import logging
import argparse
import numpy as np
import warnings

warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - TRAINER - %(message)s')
logger = logging.getLogger(__name__)

def main(model_name, n_samples=10000):
    # =========================================================================
    # 0. Kiểm tra dependencies
    # =========================================================================
    print("[*] Đang nạp Concrete ML (LLVM compiler)... Bước này có thể mất 30-60 giây.", flush=True)
    try:
        from concrete.ml.sklearn import XGBClassifier
        from concrete.ml.deployment import FHEModelDev
        print("[✓] Concrete ML đã sẵn sàng.", flush=True)

        try:
            import concrete.compiler
            if hasattr(concrete.compiler, "check_gpu_available") and concrete.compiler.check_gpu_available():
                logger.info("🚀 ĐÃ PHÁT HIỆN NVIDIA GPU (CUDA)! Sẽ biên dịch mạch FHE tối ưu cho GPU.")
            else:
                logger.info("ℹ️ Đang chạy trên CPU (chưa phát hiện backend GPU).")
        except Exception:
            pass
    except ImportError:
        logger.error("Vui lòng cài đặt concrete-ml trên Linux/WSL:")
        logger.error("  pip install concrete-ml")
        sys.exit(1)

    print("[*] Đang nạp thư viện Hugging Face Datasets...", flush=True)
    try:
        from datasets import load_dataset
        print("[✓] Hugging Face Datasets đã sẵn sàng.", flush=True)
    except ImportError:
        logger.error("Vui lòng cài đặt thư viện datasets của Hugging Face:")
        logger.error("  pip install datasets")
        sys.exit(1)

    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, accuracy_score

    base_dir = os.path.dirname(os.path.abspath(__file__))
    deploy_dir = os.path.join(base_dir, "models", model_name)
    os.makedirs(deploy_dir, exist_ok=True)

    # Thư mục lưu dataset trong project
    project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))
    data_dir = os.path.join(project_root, "data", "huggingface")
    os.makedirs(data_dir, exist_ok=True)

    # =========================================================================
    # 1. Download Dataset từ Hugging Face
    # =========================================================================
    logger.info("=" * 60)
    logger.info("BƯỚC 1: Download dataset UNSW-NB15 từ Hugging Face...")
    logger.info("  Nguồn: https://huggingface.co/datasets/rdpahalavan/UNSW-NB15")
    logger.info(f"  Lưu vào: {data_dir}")
    logger.info("  Chỉ tải Network-Flows (~183MB), KHÔNG tải Packet-Bytes (~100GB+)")
    logger.info("=" * 60)

    # CHỈ tải file Network-Flows (flow-level features), BỎ QUA Packet-Bytes (raw packet data rất nặng)
    dataset = load_dataset(
        "rdpahalavan/UNSW-NB15",
        data_files="Network-Flows/UNSW_Flow.parquet",
        split="train",
        cache_dir=data_dir
    )
    logger.info(f"  Tổng số bản ghi trong dataset: {len(dataset):,}")

    # Chuyển sang pandas DataFrame
    logger.info("  Đang chuyển sang DataFrame...")
    df = dataset.to_pandas()
    logger.info("  ✓ Đã chuyển xong.")

    # =========================================================================
    # 2. Tiền xử lý dữ liệu
    # =========================================================================
    logger.info("")
    logger.info("=" * 60)
    logger.info("BƯỚC 2: Tiền xử lý dữ liệu...")
    logger.info("=" * 60)

    # Cột cần loại bỏ (không phải feature): ID, IP addresses, timestamps, label text
    cols_to_drop = ['flow_id', 'source_ip', 'destination_ip', 'stime', 'ltime', 'attack_label']
    # Cột target
    target_col = 'binary_label'

    # Loại bỏ các cột không cần thiết
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop(columns=[col])

    logger.info(f"  Số features sau khi loại bỏ cột không cần thiết: {len(df.columns) - 1}")

    # Xác định các cột categorical và numerical
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)

    numerical_cols = [col for col in df.columns if col != target_col and col not in categorical_cols]

    logger.info(f"  Cột categorical ({len(categorical_cols)}): {categorical_cols}")
    logger.info(f"  Cột numerical ({len(numerical_cols)}): {len(numerical_cols)} cột")

    # Label Encoding cho các cột categorical
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = df[col].fillna('unknown')
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = {
            'classes': le.classes_.tolist()
        }
        logger.info(f"    Encoded '{col}': {len(le.classes_)} categories")

    # Xử lý missing values cho numerical columns
    for col in numerical_cols:
        df[col] = df[col].fillna(0)

    # Lấy danh sách feature names (đã bỏ target)
    feature_names = [col for col in df.columns if col != target_col]
    logger.info(f"  Tổng số features cho model: {len(feature_names)}")

    # Tách features và target
    X = df[feature_names].values.astype(np.float32)
    y = df[target_col].values.astype(np.int64)

    logger.info(f"  Phân bố nhãn:")
    unique, counts = np.unique(y, return_counts=True)
    for u, c in zip(unique, counts):
        label_name = "Normal" if u == 0 else "Attack"
        logger.info(f"    {label_name} (label={u}): {c:,} ({c/len(y)*100:.1f}%)")

    # Sample nếu dataset quá lớn (Concrete ML compile rất lâu với dataset lớn)
    if len(X) > n_samples:
        logger.info(f"  Sampling {n_samples:,} bản ghi để tối ưu thời gian compile FHE...")
        indices = np.random.RandomState(42).choice(len(X), size=n_samples, replace=False)
        X = X[indices]
        y = y[indices]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    logger.info(f"  Train set: {len(X_train):,} | Test set: {len(X_test):,}")

    # Chuẩn hóa features với StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Ép kiểu về float32 sau khi scale
    X_train = X_train.astype(np.float32)
    X_test = X_test.astype(np.float32)

    # =========================================================================
    # 3. Train XGBoost (Concrete ML)
    # =========================================================================
    logger.info("")
    logger.info("=" * 60)
    logger.info("BƯỚC 3: Train XGBoost Classifier (Concrete ML)...")
    logger.info("  Mô hình sẽ được lượng tử hóa tự động bởi Concrete ML")
    logger.info("=" * 60)

    model = XGBClassifier(
        n_estimators=50,
        max_depth=4,
        learning_rate=0.1,
        n_jobs=-1,
        random_state=42,
        n_bits=6  # Số bit lượng tử hóa cho FHE (6 bits = tốc độ tốt, chất lượng chấp nhận được)
    )
    model.fit(X_train, y_train)

    # Đánh giá trên cleartext (chưa mã hóa)
    y_pred_clear = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_clear)
    logger.info(f"\n  === KẾT QUẢ ĐÁNH GIÁ (Cleartext - Chưa mã hóa) ===")
    logger.info(f"  Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    logger.info(f"\n  Classification Report:")

    report = classification_report(
        y_test, y_pred_clear,
        target_names=['Normal', 'Attack'],
        digits=4
    )
    for line in report.split('\n'):
        logger.info(f"  {line}")

    # =========================================================================
    # 4. Compile sang FHE Circuit
    # =========================================================================
    logger.info("")
    logger.info("=" * 60)
    logger.info("BƯỚC 4: Compile mô hình sang mạch FHE (TFHE)...")
    logger.info("  Quá trình này sẽ:")
    logger.info("    - Lượng tử hóa (Quantization) mô hình")
    logger.info("    - Tạo bảng lookup (Programmable Bootstrapping)")
    logger.info("    - Sinh mạch FHE tối ưu")
    logger.info("  Có thể mất vài phút...")
    logger.info("=" * 60)

    model.compile(X_train)
    logger.info("  ✓ Compile thành công!")

    # =========================================================================
    # 5. Lưu Deployment Artifacts
    # =========================================================================
    logger.info("")
    logger.info("=" * 60)
    logger.info("BƯỚC 5: Lưu Deployment Artifacts...")
    logger.info("=" * 60)

    fhe_dev = FHEModelDev(path_dir=deploy_dir, model=model)
    fhe_dev.save()
    logger.info(f"  ✓ Đã lưu client.zip + server.zip vào: {deploy_dir}")

    # Lưu preprocessing metadata
    metadata = {
        'feature_names': feature_names,
        'categorical_cols': categorical_cols,
        'label_encoders': label_encoders,
        'scaler_mean': scaler.mean_.tolist(),
        'scaler_scale': scaler.scale_.tolist(),
        'target_names': ['Normal', 'Attack'],
        'dataset_source': 'rdpahalavan/UNSW-NB15',
        'n_features': len(feature_names),
        'n_samples_trained': len(X_train),
        'accuracy_cleartext': float(accuracy),
        'model_params': {
            'n_estimators': 50,
            'max_depth': 4,
            'learning_rate': 0.1,
            'n_bits': 6
        }
    }

    metadata_path = os.path.join(deploy_dir, "preprocessing_metadata.json")
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    logger.info(f"  ✓ Đã lưu preprocessing metadata vào: {metadata_path}")

    # Lưu một vài mẫu test để demo
    sample_indices = np.random.RandomState(99).choice(len(X_test), size=min(10, len(X_test)), replace=False)
    sample_data = {
        'samples': X_test[sample_indices].tolist(),
        'labels': y_test[sample_indices].tolist(),
        'descriptions': []
    }
    for idx, label in enumerate(y_test[sample_indices]):
        desc = "Normal Traffic" if label == 0 else "Attack Traffic"
        sample_data['descriptions'].append(f"Sample {idx+1}: {desc}")

    samples_path = os.path.join(deploy_dir, "sample_inputs.json")
    with open(samples_path, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=4)
    logger.info(f"  ✓ Đã lưu {len(sample_indices)} mẫu test demo vào: {samples_path}")

    # =========================================================================
    # Tổng kết
    # =========================================================================
    logger.info("")
    logger.info("=" * 60)
    logger.info("HOÀN TẤT! Mô hình đã sẵn sàng cho FHE Inference.")
    logger.info("=" * 60)
    logger.info(f"  Dataset: UNSW-NB15 (Hugging Face)")
    logger.info(f"  Bài toán: Binary Classification (Normal vs Attack)")
    logger.info(f"  Số features: {len(feature_names)}")
    logger.info(f"  Accuracy (Cleartext): {accuracy*100:.2f}%")
    logger.info(f"  Thư mục output: {deploy_dir}")
    logger.info("")
    logger.info("Chạy inference FHE:")
    logger.info("  python3 src/main.py --model unsw_nb15_xgb --platform concrete_ml")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train & Compile XGBoost trên UNSW-NB15 cho Concrete ML FHE"
    )
    parser.add_argument(
        "--model", type=str, default="unsw_nb15_xgb",
        help="Tên thư mục output cho mô hình (mặc định: unsw_nb15_xgb)"
    )
    parser.add_argument(
        "--n-samples", type=int, default=10000,
        help="Số lượng mẫu tối đa để train (mặc định: 10000, giảm để compile nhanh hơn)"
    )
    args = parser.parse_args()
    main(args.model, args.n_samples)
