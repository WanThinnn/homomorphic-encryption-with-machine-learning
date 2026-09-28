"""
UEBA CKKS Inference (OpenFHE)

Performs privacy-preserving UEBA inference using the CKKS scheme.
Loads trained model weights and runs homomorphic linear algebra on encrypted
behavioral vectors.

Supports:
  - Logistic Regression: Enc(W·x + b) → decrypt → sigmoid → score
  - MLP: Enc(W₁·x + b₁) → Enc(x²) → Enc(W₂·z + b₂) → ... → decrypt → sigmoid
"""
import os
import sys
import json
import time
import logging
import numpy as np
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

# Add lib path for openfhe.pyd on Windows
SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if sys.platform != 'linux':
    lib_path = os.path.join(SRC_DIR, "lib")
    if lib_path not in sys.path:
        sys.path.insert(0, lib_path)

from crypto.homomorphic_encryption import FHEPipeline


def _infer_lr_ckks(
    fhe: FHEPipeline,
    weights: List[float],
    bias: float,
    X_test: np.ndarray,
    n_samples: int,
) -> Dict[str, Any]:
    """
    Run Logistic Regression inference on encrypted data using CKKS.

    Steps:
      1. Encode weights as plaintext
      2. For each sample: encrypt → EvalMult → EvalSum → EvalAdd bias → decrypt
      3. Apply sigmoid on decrypted logit (client-side)
    """
    results = {
        "predictions": [],
        "encrypt_times": [],
        "inference_times": [],
        "decrypt_times": [],
    }

    # Pre-encode weights and bias
    encoded_weights = fhe.encode_vector(weights)
    bias_vector = [bias] * len(weights)
    encoded_bias = fhe.encode_vector(bias_vector)

    for i in range(min(n_samples, len(X_test))):
        x = X_test[i].tolist()

        # Encrypt
        t0 = time.perf_counter()
        enc_x = fhe.encrypt_vector(x)
        t_enc = time.perf_counter() - t0

        # Homomorphic inference: W·x + b
        t0 = time.perf_counter()
        mult_result = fhe.eval_mult(enc_x, encoded_weights)
        sum_result = fhe.eval_sum(mult_result)
        final_result = fhe.eval_add(sum_result, encoded_bias)
        t_inf = time.perf_counter() - t0

        # Decrypt
        t0 = time.perf_counter()
        dec = fhe.decrypt_vector(final_result)
        logit = dec[0]
        t_dec = time.perf_counter() - t0

        # Sigmoid (client-side)
        import math
        prob = 1 / (1 + math.exp(-max(-500, min(500, logit))))

        results["predictions"].append({"logit": logit, "prob": prob, "label": int(prob > 0.5)})
        results["encrypt_times"].append(t_enc)
        results["inference_times"].append(t_inf)
        results["decrypt_times"].append(t_dec)

        if (i + 1) % 5 == 0 or i == 0:
            logger.info(
                f"  Sample {i+1}/{n_samples} | "
                f"enc={t_enc*1000:.1f}ms | inf={t_inf*1000:.1f}ms | dec={t_dec*1000:.1f}ms | "
                f"prob={prob:.4f}"
            )

    return results


def run_ckks_inference(
    model_type: str,
    data_dir: str,
    model_dir: str,
    n_samples: int = 10,
):
    """Main entry point for CKKS-based FHE inference."""
    logger.info("=" * 60)
    logger.info("  CKKS FHE INFERENCE (OpenFHE)")
    logger.info("=" * 60)

    # Load test data
    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))

    n_features = X_test.shape[1]
    logger.info(f"Test data: {X_test.shape}, running {n_samples} samples")

    if model_type == "lr":
        # Load weights
        weights_path = os.path.join(model_dir, "ueba_lr", "weights.json")
        with open(weights_path, "r") as f:
            w = json.load(f)
        weights = w["weights"]
        bias = w["bias"]

        # Init FHE (mult_depth=2 sufficient for LR)
        logger.info("Initializing CKKS context (mult_depth=2)...")
        t0 = time.perf_counter()
        fhe = FHEPipeline(
            mult_depth=2,
            scale_mod_size=40,
            batch_size=0,
            vector_dim=n_features,
        )
        fhe.generate_keys()
        t_keygen = time.perf_counter() - t0
        logger.info(f"Key generation: {t_keygen:.2f}s")

        # Run inference
        results = _infer_lr_ckks(fhe, weights, bias, X_test, n_samples)

    elif model_type == "mlp":
        # MLP requires higher depth for square activations
        weights_path = os.path.join(model_dir, "ueba_mlp", "weights.json")
        with open(weights_path, "r") as f:
            w = json.load(f)

        logger.info("Initializing CKKS context (mult_depth=6 for MLP)...")
        t0 = time.perf_counter()
        fhe = FHEPipeline(
            mult_depth=6,
            scale_mod_size=40,
            batch_size=0,
            vector_dim=n_features,
        )
        fhe.generate_keys()
        t_keygen = time.perf_counter() - t0
        logger.info(f"Key generation: {t_keygen:.2f}s")

        # TODO: Implement MLP CKKS inference (layer-by-layer homomorphic computation)
        logger.warning("MLP CKKS inference not yet implemented. Use Concrete ML instead.")
        results = {"predictions": [], "encrypt_times": [], "inference_times": [], "decrypt_times": []}

    else:
        logger.error(f"Unknown model: {model_type}")
        return

    # Summary
    if results["predictions"]:
        avg_enc = np.mean(results["encrypt_times"]) * 1000
        avg_inf = np.mean(results["inference_times"]) * 1000
        avg_dec = np.mean(results["decrypt_times"]) * 1000
        avg_total = avg_enc + avg_inf + avg_dec

        print("\n" + "=" * 60)
        print(f"  CKKS INFERENCE SUMMARY — {model_type.upper()}")
        print("=" * 60)
        print(f"  Samples:          {len(results['predictions'])}")
        print(f"  Avg Encrypt:      {avg_enc:.1f} ms")
        print(f"  Avg Inference:    {avg_inf:.1f} ms")
        print(f"  Avg Decrypt:      {avg_dec:.1f} ms")
        print(f"  Avg Total (E2E):  {avg_total:.1f} ms")
        print("=" * 60)

        # Compare with ground truth
        preds = [p["label"] for p in results["predictions"]]
        labels = y_test[:len(preds)]
        correct = sum(1 for p, l in zip(preds, labels) if p == l)
        print(f"  Accuracy (on {len(preds)} samples): {correct/len(preds)*100:.1f}%")
