"""
CERT Data Preprocessor

Takes the extracted behavioral_features.csv and produces train/val/test splits
with normalization and class imbalance handling.

Output files in data/cert/processed/:
  - X_train.npy, y_train.npy
  - X_val.npy, y_val.npy
  - X_test.npy, y_test.npy
  - scaler.pkl (fitted MinMaxScaler for CKKS compatibility)
  - feature_names.json
"""
import os
import json
import logging
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

logger = logging.getLogger(__name__)

FEATURE_COLUMNS = [
    "login_count",
    "logoff_count",
    "after_hours_login",
    "unique_machines",
    "file_copy_count",
    "file_write_count",
    "file_delete_count",
    "file_exe_count",
    "email_sent",
    "email_external",
    "email_attachments",
    "email_bcc_count",
    "usb_connect",
    "usb_disconnect",
    "http_requests",
    "unique_urls",
    "unique_domains",
]


def preprocess(
    data_dir: str,
    test_size: float = 0.15,
    val_size: float = 0.15,
    random_state: int = 42,
    use_smote: bool = True,
):
    """
    Preprocess behavioral_features.csv:
      1. Load features
      2. Normalize with MinMaxScaler [0, 1] (CKKS-friendly)
      3. Split into train/val/test
      4. Optionally apply SMOTE for class imbalance
      5. Save numpy arrays and artifacts
    """
    csv_path = os.path.join(data_dir, "behavioral_features.csv")
    if not os.path.exists(csv_path):
        logger.error(f"behavioral_features.csv not found at {csv_path}")
        logger.error("Run feature extraction first: python src/main.py prepare-data")
        return

    logger.info(f"Loading features from {csv_path}...")
    df = pd.read_csv(csv_path)

    X = df[FEATURE_COLUMNS].values.astype(np.float32)
    y = df["label"].values.astype(np.int32)

    logger.info(f"Dataset shape: {X.shape}")
    logger.info(f"Class distribution: normal={np.sum(y==0)}, malicious={np.sum(y==1)}")
    logger.info(f"Imbalance ratio: {np.sum(y==0) / max(np.sum(y==1), 1):.1f}:1")

    # Split: first split off test, then split remainder into train/val
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    relative_val_size = val_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=relative_val_size, random_state=random_state, stratify=y_temp
    )

    logger.info(f"Split sizes: train={len(X_train)}, val={len(X_val)}, test={len(X_test)}")

    # Normalize with MinMaxScaler — fitted on train only
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    # Handle class imbalance with SMOTE (train only)
    if use_smote and np.sum(y_train == 1) > 0:
        try:
            from imblearn.over_sampling import SMOTE
            smote = SMOTE(random_state=random_state)
            X_train, y_train = smote.fit_resample(X_train, y_train)
            logger.info(f"After SMOTE: train={len(X_train)} (normal={np.sum(y_train==0)}, malicious={np.sum(y_train==1)})")
        except ImportError:
            logger.warning("imblearn not installed. Skipping SMOTE. Install: pip install imbalanced-learn")

    # Save
    np.save(os.path.join(data_dir, "X_train.npy"), X_train.astype(np.float32))
    np.save(os.path.join(data_dir, "y_train.npy"), y_train.astype(np.int32))
    np.save(os.path.join(data_dir, "X_val.npy"), X_val.astype(np.float32))
    np.save(os.path.join(data_dir, "y_val.npy"), y_val.astype(np.int32))
    np.save(os.path.join(data_dir, "X_test.npy"), X_test.astype(np.float32))
    np.save(os.path.join(data_dir, "y_test.npy"), y_test.astype(np.int32))

    # Save scaler
    with open(os.path.join(data_dir, "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)

    # Save feature names
    with open(os.path.join(data_dir, "feature_names.json"), "w") as f:
        json.dump(FEATURE_COLUMNS, f, indent=2)

    logger.info("Preprocessing complete!")
    logger.info(f"Files saved to: {data_dir}")


if __name__ == "__main__":
    import sys
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "..", "data", "cert", "processed")
    preprocess(d)
