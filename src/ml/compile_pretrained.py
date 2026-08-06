import os
import sys
import numpy as np
import logging
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

import argparse

try:
    from concrete.ml.sklearn import XGBClassifier
    from concrete.ml.deployment import FHEModelDev
except ImportError:
    print("Vui lòng cài đặt concrete-ml trên Linux/WSL (pip install concrete-ml)")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - COMPILER - %(message)s')

def main(model_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    deploy_dir = os.path.join(base_dir, "models", model_name)
    
    os.makedirs(deploy_dir, exist_ok=True)
    
    logging.info("1. Tạo mô hình XGBoost (Mô phỏng tải mô hình Pre-trained)...")
    # Chúng ta tạo bộ dữ liệu giả 256 chiều (tương tự như Vector TF-IDF của ta)
    X, y = make_classification(n_samples=500, n_features=256, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train siêu tốc
    model = XGBClassifier(n_estimators=10, max_depth=3, n_jobs=-1)
    model.fit(X_train, y_train)
    
    logging.info("2. Bắt đầu Compile sang mạch FHE (TFHE). Quá trình này tính toán lượng tử hóa...")
    # Cần cung cấp tập dữ liệu mẫu (Representative Dataset) để FHE compiler phân tích giới hạn của các nốt
    model.compile(X_train)
    
    logging.info("3. Lưu các tệp tin Deployment (FHE Specs, Weights) ra thư mục models/concrete_pretrained...")
    fhe_dev = FHEModelDev(path_dir=deploy_dir, model=model)
    fhe_dev.save()
    
    logging.info("Hoàn tất! Mạch FHE đã được lưu. Giờ đây Client và Server có thể chạy mà không cần train lại.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="concrete_pretrained", help="Tên mô hình để biên dịch")
    args = parser.parse_args()
    main(args.model)
