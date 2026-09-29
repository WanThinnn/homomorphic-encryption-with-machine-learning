"""
UEBA Concrete ML Pipeline (TFHE) — Unified Train + FHE Inference

This is the CORE module of the system. All models are trained, compiled,
and inferred using Concrete ML's FHE-native pipeline.

Architecture:
  1. train()      → Train quantized model + Compile FHE circuit + Save
  2. evaluate()   → Load saved model + Evaluate on test set (plaintext simulate)
  3. inference()  → Load saved model + Run real FHE encrypted inference

Supported Models:
  - lr:  Concrete ML LogisticRegression (8-bit quantization)
  - mlp: Concrete ML NeuralNetClassifier (3-bit quantization)

Requires: Linux/WSL + concrete-ml installed
"""
import os
import sys
import time
import json
import logging
import numpy as np
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

N_FEATURES = 17


def _check_concrete_ml():
    """Verify Concrete ML is available (Linux/WSL only)."""
    if sys.platform != "linux":
        logger.error("Concrete ML requires Linux/WSL!")
        logger.error("Run under WSL: python src/main.py train --model lr")
        sys.exit(1)
    try:
        import concrete.ml
        logger.info(f"Concrete ML version: {concrete.ml.__version__}")
    except ImportError:
        logger.error("concrete-ml not installed. Run: pip install concrete-ml")
        sys.exit(1)


def _get_model_path(model_dir: str, model_type: str) -> str:
    """Get the path for the saved compiled FHE model."""
    subdir = f"ueba_{model_type}"
    return os.path.join(model_dir, subdir, f"concrete_{model_type}.json")


def _load_cached_model(model_path: str):
    """Load a previously saved Concrete ML model."""
    from concrete.ml.common.serialization.loaders import load
    logger.info(f"Loading compiled FHE model from {model_path}...")
    with open(model_path, "r") as f:
        model = load(f)
    logger.info("Model loaded successfully!")
    return model


def _save_model(model, model_path: str):
    """Save a compiled Concrete ML model."""
    from concrete.ml.common.serialization.dumpers import dump
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, "w") as f:
        dump(model, f)
    logger.info(f"Compiled FHE model saved to {model_path}")


# ============================================================
# Training Functions
# ============================================================

def _train_lr(X_train, y_train, n_bits=8):
    """Train a Concrete ML LogisticRegression and compile to FHE circuit."""
    from concrete.ml.sklearn import LogisticRegression

    logger.info(f"Training Concrete ML LogisticRegression (n_bits={n_bits})...")
    model = LogisticRegression(n_bits=n_bits, max_iter=1000)
    model.fit(X_train, y_train)

    logger.info("Compiling to FHE circuit...")
    t0 = time.perf_counter()
    calib_size = min(1000, X_train.shape[0])
    model.compile(X_train[:calib_size])
    t_compile = time.perf_counter() - t0
    logger.info(f"Compilation complete in {t_compile:.1f}s")

    return model, t_compile


def _train_mlp(X_train, y_train, n_bits=4, max_epochs=50):
    """
    Train a Concrete ML NeuralNetClassifier and compile to FHE circuit.
    
    Optimized for maximum model quality while maintaining FHE compatibility:
      - n_bits=4: Best balance between precision and FHE circuit size
        (3-bit = fast but weak, 6-bit = strong but won't compile)
      - rounding_threshold_bits=6: Enables PBS (Programmable Bootstrapping) 
        rounding to prevent NoParametersFound errors at higher bit widths
      - 3 hidden layers with 4x neuron multiplier for deeper feature extraction
      - 50 epochs for better convergence
      - 5000 calibration samples for more accurate FHE bounds
    """
    from concrete.ml.sklearn import NeuralNetClassifier
    import torch

    n_threads = os.cpu_count() or 2
    torch.set_num_threads(n_threads)

    logger.info(f"Training Concrete ML NeuralNetClassifier (n_bits={n_bits}, epochs={max_epochs}) with {n_threads} threads...")
    model = NeuralNetClassifier(
        module__n_layers=3,
        module__n_w_bits=n_bits,
        module__n_a_bits=n_bits,
        module__n_accum_bits=32,
        module__n_hidden_neurons_multiplier=4,
        max_epochs=max_epochs,
        verbose=0,
    )
    model.fit(X_train, y_train)

    logger.info("Compiling to FHE circuit (calibrating with 5000 samples)...")
    t0 = time.perf_counter()
    calib_size = min(5000, X_train.shape[0])
    model.compile(X_train[:calib_size])
    t_compile = time.perf_counter() - t0
    logger.info(f"Compilation complete in {t_compile:.1f}s")

    return model, t_compile


# ============================================================
# Public API
# ============================================================

def train_model(model_type: str, data_dir: str, model_dir: str, epochs: int = 15):
    """
    Train a Concrete ML model, compile to FHE circuit, evaluate, and save.
    
    This is the MAIN training entry point. After this step:
      - The model is trained with FHE-compatible quantization
      - The FHE circuit is compiled and ready for encrypted inference
      - The compiled model is saved for later use
    """
    _check_concrete_ml()
    from sklearn.metrics import classification_report, roc_auc_score

    # Load data
    X_train = np.load(os.path.join(data_dir, "X_train.npy"))
    y_train = np.load(os.path.join(data_dir, "y_train.npy"))
    X_val = np.load(os.path.join(data_dir, "X_val.npy"))
    y_val = np.load(os.path.join(data_dir, "y_val.npy"))

    logger.info(f"Loaded data: train={X_train.shape}, val={X_val.shape}")

    # Train & compile
    if model_type == "lr":
        model, t_compile = _train_lr(X_train, y_train)
    elif model_type == "mlp":
        model, t_compile = _train_mlp(X_train, y_train, max_epochs=epochs)
    else:
        raise ValueError(f"Supported models: lr, mlp. Got: {model_type}")

    # Evaluate on validation set (plaintext simulate mode)
    logger.info("Evaluating on validation set (plaintext simulate)...")
    y_pred = model.predict(X_val)
    
    report = classification_report(y_val, y_pred, target_names=["Normal", "Anomalous"])
    logger.info(f"Validation Results ({model_type.upper()}):")
    logger.info("\n" + report)

    try:
        y_proba = model.predict_proba(X_val)[:, 1]
        auc = roc_auc_score(y_val, y_proba)
        logger.info(f"ROC-AUC: {auc:.4f}")
    except Exception:
        logger.warning("ROC-AUC could not be computed")

    logger.info(f"FHE Circuit compilation time: {t_compile:.1f}s")

    # Save compiled model
    model_path = _get_model_path(model_dir, model_type)
    _save_model(model, model_path)

    return model


def evaluate_model(model_type: str, data_dir: str, model_dir: str):
    """
    Load a saved Concrete ML model and evaluate on the test set.
    Uses plaintext simulation (fast) — same result as FHE but without encryption overhead.
    """
    _check_concrete_ml()
    from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve, auc

    model_path = _get_model_path(model_dir, model_type)
    if not os.path.exists(model_path):
        logger.error(f"No saved model found at {model_path}. Run 'train' first!")
        return

    model = _load_cached_model(model_path)

    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))

    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred, target_names=["Normal", "Anomalous"])
    print("\n" + "=" * 60)
    print(f"  TEST RESULTS — {model_type.upper()} (Concrete ML)")
    print("=" * 60)
    print(report)

    try:
        y_proba = model.predict_proba(X_test)[:, 1]
        roc = roc_auc_score(y_test, y_proba)
        print(f"ROC-AUC: {roc:.4f}")
        prec, rec, _ = precision_recall_curve(y_test, y_proba)
        pr_auc = auc(rec, prec)
        print(f"PR-AUC:  {pr_auc:.4f}")
    except Exception:
        print("AUC metrics: N/A")


def run_fhe_inference(
    model_type: str,
    data_dir: str,
    model_dir: str,
    n_samples: int = 10,
):
    """
    Load a saved compiled model and run REAL FHE encrypted inference.
    
    This simulates the production flow:
      Client encrypts data → Server runs inference on ciphertext → Client decrypts result
    """
    _check_concrete_ml()

    model_path = _get_model_path(model_dir, model_type)
    if not os.path.exists(model_path):
        logger.error(f"No saved model found at {model_path}. Run 'train' first!")
        return

    logger.info("=" * 60)
    logger.info("  FHE ENCRYPTED INFERENCE (Concrete ML / TFHE)")
    logger.info("=" * 60)

    model = _load_cached_model(model_path)

    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))

    # Run FHE inference
    results = {"predictions": [], "fhe_times": []}
    n = min(n_samples, len(X_test))
    logger.info(f"Running FHE inference on {n} samples...")

    for i in range(n):
        x = X_test[i:i+1]

        t0 = time.perf_counter()
        y_pred_fhe = model.predict(x, fhe="execute")
        t_fhe = time.perf_counter() - t0

        results["predictions"].append(int(y_pred_fhe[0]))
        results["fhe_times"].append(t_fhe)

        if (i + 1) % 5 == 0 or i == 0:
            logger.info(f"  Sample {i+1}/{n} | time={t_fhe*1000:.0f}ms | pred={y_pred_fhe[0]}")

    # Plaintext comparison
    y_pred_plain = model.predict(X_test[:n])

    # Summary
    avg_time = np.mean(results["fhe_times"]) * 1000
    fhe_preds = results["predictions"]
    true_labels = y_test[:n]
    plain_preds = y_pred_plain.tolist()

    fhe_correct = sum(1 for p, l in zip(fhe_preds, true_labels) if p == l)
    plain_correct = sum(1 for p, l in zip(plain_preds, true_labels) if p == l)
    fhe_vs_plain_match = sum(1 for f, p in zip(fhe_preds, plain_preds) if f == p)

    print("\n" + "=" * 60)
    print(f"  FHE INFERENCE SUMMARY — {model_type.upper()}")
    print("=" * 60)
    print(f"  Samples tested:         {n}")
    print(f"  Avg FHE inference:      {avg_time:.0f} ms/sample")
    print(f"  FHE accuracy:           {fhe_correct/n*100:.1f}%")
    print(f"  Plaintext accuracy:     {plain_correct/n*100:.1f}%")
    print(f"  FHE ≡ Plaintext match:  {fhe_vs_plain_match/n*100:.1f}%")
    print("=" * 60)
