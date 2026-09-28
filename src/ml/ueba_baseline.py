"""
UEBA Plaintext ML Baseline

Trains and evaluates Logistic Regression and MLP models on plaintext
behavioral features. These serve as the upper-bound baseline for comparing
FHE inference performance.

Models:
  - lr:          Logistic Regression (scikit-learn)
  - mlp:         2-layer MLP with square activation (PyTorch)
  - autoencoder: Autoencoder for unsupervised anomaly detection (PyTorch)
"""
import os
import json
import logging
import numpy as np
import pickle
from typing import Optional

logger = logging.getLogger(__name__)

N_FEATURES = 17  # Number of behavioral features


# ============================================================
# Logistic Regression
# ============================================================

def _train_lr(X_train, y_train, X_val, y_val, output_dir):
    """Train a Logistic Regression model using scikit-learn."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report, roc_auc_score

    logger.info("Training Logistic Regression...")
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42,
    )
    model.fit(X_train, y_train)

    # Evaluate on validation
    y_pred = model.predict(X_val)
    y_proba = model.predict_proba(X_val)[:, 1]

    logger.info("Validation Results (Logistic Regression):")
    report = classification_report(y_val, y_pred, target_names=["Normal", "Anomalous"])
    logger.info("\n" + report)

    try:
        auc = roc_auc_score(y_val, y_proba)
        logger.info(f"ROC-AUC: {auc:.4f}")
    except ValueError:
        auc = 0.0
        logger.warning("ROC-AUC could not be computed (single class in y_val?)")

    # Save model
    model_dir = os.path.join(output_dir, "ueba_lr")
    os.makedirs(model_dir, exist_ok=True)

    # Save as pickle for sklearn
    with open(os.path.join(model_dir, "model.pkl"), "wb") as f:
        pickle.dump(model, f)

    # Also save weights as JSON for OpenFHE CKKS manual inference
    weights_data = {
        "weights": model.coef_[0].tolist(),
        "bias": float(model.intercept_[0]),
        "n_features": N_FEATURES,
        "model_type": "logistic_regression",
    }
    with open(os.path.join(model_dir, "weights.json"), "w") as f:
        json.dump(weights_data, f, indent=2)

    logger.info(f"LR model saved to {model_dir}")
    return model


# ============================================================
# MLP with Square Activation (FHE-friendly)
# ============================================================

class SquareActivation:
    """Square activation function: f(x) = x², FHE-friendly (degree-2 polynomial)."""
    pass


def _train_mlp(X_train, y_train, X_val, y_val, output_dir, epochs=100):
    """Train a 2-layer MLP with square activation using PyTorch."""
    import torch
    import torch.nn as nn
    from torch.utils.data import TensorDataset, DataLoader
    from sklearn.metrics import classification_report, roc_auc_score

    class SquareAct(nn.Module):
        """x² activation — FHE-friendly, only adds 1 multiplicative depth."""
        def forward(self, x):
            return x * x

    class UEBAMLP(nn.Module):
        """MLP: Input(17) → Dense(32) → x² → Dense(16) → x² → Dense(1)"""
        def __init__(self):
            super().__init__()
            self.net = nn.Sequential(
                nn.Linear(N_FEATURES, 32),
                SquareAct(),
                nn.Linear(32, 16),
                SquareAct(),
                nn.Linear(16, 1),
            )

        def forward(self, x):
            return self.net(x).squeeze(-1)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Training MLP on {device}...")

    model = UEBAMLP().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)

    # Class-weighted BCE loss
    pos_weight = torch.tensor([len(y_train[y_train == 0]) / max(len(y_train[y_train == 1]), 1)])
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight.to(device))

    # DataLoaders
    train_ds = TensorDataset(
        torch.tensor(X_train, dtype=torch.float32),
        torch.tensor(y_train, dtype=torch.float32),
    )
    val_ds = TensorDataset(
        torch.tensor(X_val, dtype=torch.float32),
        torch.tensor(y_val, dtype=torch.float32),
    )
    train_loader = DataLoader(train_ds, batch_size=256, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=256, shuffle=False)

    # Training loop
    best_auc = 0
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            logits = model(xb)
            loss = criterion(logits, yb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        # Validate every 10 epochs
        if (epoch + 1) % 10 == 0:
            model.eval()
            all_proba = []
            all_labels = []
            with torch.no_grad():
                for xb, yb in val_loader:
                    xb = xb.to(device)
                    logits = model(xb)
                    proba = torch.sigmoid(logits).cpu().numpy()
                    all_proba.extend(proba)
                    all_labels.extend(yb.numpy())

            try:
                auc = roc_auc_score(all_labels, all_proba)
            except ValueError:
                auc = 0.0

            logger.info(f"Epoch {epoch+1}/{epochs} | Loss: {total_loss/len(train_loader):.4f} | Val AUC: {auc:.4f}")

            if auc > best_auc:
                best_auc = auc
                best_state = model.state_dict()

    # Load best model
    if best_auc > 0:
        model.load_state_dict(best_state)

    # Final evaluation
    model.eval()
    all_proba = []
    all_labels = []
    with torch.no_grad():
        for xb, yb in val_loader:
            xb = xb.to(device)
            logits = model(xb)
            proba = torch.sigmoid(logits).cpu().numpy()
            all_proba.extend(proba)
            all_labels.extend(yb.numpy())

    y_pred = [1 if p > 0.5 else 0 for p in all_proba]
    report = classification_report(all_labels, y_pred, target_names=["Normal", "Anomalous"])
    logger.info("Validation Results (MLP):")
    logger.info("\n" + report)

    # Save model
    model_dir = os.path.join(output_dir, "ueba_mlp")
    os.makedirs(model_dir, exist_ok=True)

    torch.save(model.state_dict(), os.path.join(model_dir, "model.pt"))

    # Export weights as JSON for CKKS manual inference
    state = model.cpu().state_dict()
    weights_data = {
        "model_type": "mlp",
        "architecture": "17-32-16-1",
        "activation": "square",
        "layers": [],
    }
    layer_idx = 0
    for name, param in state.items():
        if "weight" in name:
            weights_data["layers"].append({
                "name": f"layer_{layer_idx}",
                "type": "linear",
                "weight": param.numpy().tolist(),
            })
        elif "bias" in name:
            weights_data["layers"][-1]["bias"] = param.numpy().tolist()
            layer_idx += 1

    with open(os.path.join(model_dir, "weights.json"), "w") as f:
        json.dump(weights_data, f)

    logger.info(f"MLP model saved to {model_dir}")
    return model


# ============================================================
# Public API
# ============================================================

def train_model(model_type: str, data_dir: str, output_dir: str, epochs: int = 100):
    """Train a specified model type."""
    X_train = np.load(os.path.join(data_dir, "X_train.npy"))
    y_train = np.load(os.path.join(data_dir, "y_train.npy"))
    X_val = np.load(os.path.join(data_dir, "X_val.npy"))
    y_val = np.load(os.path.join(data_dir, "y_val.npy"))

    logger.info(f"Loaded data: train={X_train.shape}, val={X_val.shape}")

    if model_type == "lr":
        return _train_lr(X_train, y_train, X_val, y_val, output_dir)
    elif model_type == "mlp":
        return _train_mlp(X_train, y_train, X_val, y_val, output_dir, epochs)
    else:
        logger.error(f"Unknown model type: {model_type}")
        raise ValueError(f"Supported: lr, mlp. Got: {model_type}")


def evaluate_model(model_type: str, data_dir: str, model_dir: str):
    """Evaluate a trained model on the test set."""
    from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve, auc

    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))

    if model_type == "lr":
        with open(os.path.join(model_dir, "ueba_lr", "model.pkl"), "rb") as f:
            model = pickle.load(f)
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]
    elif model_type == "mlp":
        import torch
        import torch.nn as nn

        class SquareAct(nn.Module):
            def forward(self, x):
                return x * x

        class UEBAMLP(nn.Module):
            def __init__(self):
                super().__init__()
                self.net = nn.Sequential(
                    nn.Linear(N_FEATURES, 32),
                    SquareAct(),
                    nn.Linear(32, 16),
                    SquareAct(),
                    nn.Linear(16, 1),
                )
            def forward(self, x):
                return self.net(x).squeeze(-1)

        model = UEBAMLP()
        model.load_state_dict(torch.load(os.path.join(model_dir, "ueba_mlp", "model.pt"), weights_only=True))
        model.eval()

        with torch.no_grad():
            logits = model(torch.tensor(X_test, dtype=torch.float32))
            y_proba = torch.sigmoid(logits).numpy()
        y_pred = (y_proba > 0.5).astype(int)
    else:
        raise ValueError(f"Unknown model: {model_type}")

    # Metrics
    report = classification_report(y_test, y_pred, target_names=["Normal", "Anomalous"])
    print("\n" + "=" * 60)
    print(f"  TEST RESULTS — {model_type.upper()}")
    print("=" * 60)
    print(report)

    try:
        roc = roc_auc_score(y_test, y_proba)
        print(f"ROC-AUC: {roc:.4f}")
    except ValueError:
        print("ROC-AUC: N/A")

    try:
        prec, rec, _ = precision_recall_curve(y_test, y_proba)
        pr_auc = auc(rec, prec)
        print(f"PR-AUC:  {pr_auc:.4f}")
    except ValueError:
        print("PR-AUC: N/A")
