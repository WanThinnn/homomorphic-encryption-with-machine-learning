"""
UEBA Concrete ML Pipeline (TFHE)

Uses Zama's Concrete ML to compile scikit-learn / torch models into FHE circuits
and run privacy-preserving inference on encrypted behavioral vectors.

Supports:
  - Logistic Regression (ConcreteML LogisticRegression)
  - MLP (ConcreteML NeuralNetClassifier)

Requires: Linux/WSL + concrete-ml installed
"""
import os
import sys
import time
import json
import logging
import numpy as np
from typing import Dict, Any

logger = logging.getLogger(__name__)


def _check_concrete_ml():
    """Verify Concrete ML is available (Linux/WSL only)."""
    if sys.platform != "linux":
        logger.error("Concrete ML requires Linux/WSL!")
        logger.error("Run this command under WSL: python src/main.py fhe-inference --platform concrete")
        sys.exit(1)
    try:
        import concrete.ml
        logger.info(f"Concrete ML version: {concrete.ml.__version__}")
    except ImportError:
        logger.error("concrete-ml not installed. Run: pip install concrete-ml")
        sys.exit(1)


def _train_and_compile_lr(X_train, y_train, n_bits=8):
    """Train a Concrete ML LogisticRegression and compile to FHE circuit."""
    from concrete.ml.sklearn import LogisticRegression

    logger.info(f"Training Concrete ML LogisticRegression (n_bits={n_bits})...")
    model = LogisticRegression(n_bits=n_bits, max_iter=1000)
    model.fit(X_train, y_train)

    logger.info("Compiling to FHE circuit...")
    t0 = time.perf_counter()
    model.compile(X_train)
    t_compile = time.perf_counter() - t0
    logger.info(f"Compilation complete in {t_compile:.1f}s")

    return model, t_compile


def _train_and_compile_mlp(X_train, y_train, n_bits=6):
    """Train a Concrete ML NeuralNetClassifier and compile to FHE circuit."""
    from concrete.ml.sklearn import NeuralNetClassifier
    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Training Concrete ML NeuralNetClassifier (n_bits={n_bits}) on {device}...")
    model = NeuralNetClassifier(
        module__n_layers=2,
        module__n_w_bits=n_bits,
        module__n_a_bits=n_bits,
        module__n_accum_bits=32,
        module__n_hidden_neurons_multiplier=2,
        max_epochs=50,
        device=device,
        verbose=0,
    )
    model.fit(X_train, y_train)

    logger.info("Compiling to FHE circuit (calibrating with 1000 samples)...")
    t0 = time.perf_counter()
    # CRITICAL FIX: Only pass a subset to compile() for bounds calibration, 
    # passing 460,000 samples will freeze the CPU for hours!
    calib_size = min(1000, X_train.shape[0])
    model.compile(X_train[:calib_size])
    t_compile = time.perf_counter() - t0
    logger.info(f"Compilation complete in {t_compile:.1f}s")

    return model, t_compile


def run_concrete_inference(
    model_type: str,
    data_dir: str,
    model_dir: str,
    n_samples: int = 10,
):
    """Main entry point for Concrete ML (TFHE) inference."""
    _check_concrete_ml()

    logger.info("=" * 60)
    logger.info("  CONCRETE ML FHE INFERENCE (TFHE)")
    logger.info("=" * 60)

    # Load data
    X_train = np.load(os.path.join(data_dir, "X_train.npy"))
    y_train = np.load(os.path.join(data_dir, "y_train.npy"))
    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))

    logger.info(f"Train: {X_train.shape}, Test: {X_test.shape}")

    # Train & compile
    if model_type == "lr":
        model, t_compile = _train_and_compile_lr(X_train, y_train)
    elif model_type == "mlp":
        model, t_compile = _train_and_compile_mlp(X_train, y_train)
    else:
        logger.error(f"Unknown model: {model_type}")
        return

    # Run FHE inference on test samples
    results = {
        "predictions": [],
        "fhe_times": [],
    }

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

    # Also run plaintext (simulate) for comparison
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
    print(f"  CONCRETE ML (TFHE) SUMMARY — {model_type.upper()}")
    print("=" * 60)
    print(f"  Compilation time:       {t_compile:.1f}s")
    print(f"  Samples tested:         {n}")
    print(f"  Avg FHE inference:      {avg_time:.0f} ms/sample")
    print(f"  FHE accuracy:           {fhe_correct/n*100:.1f}%")
    print(f"  Plaintext accuracy:     {plain_correct/n*100:.1f}%")
    print(f"  FHE ≡ Plaintext match:  {fhe_vs_plain_match/n*100:.1f}%")
    print("=" * 60)
