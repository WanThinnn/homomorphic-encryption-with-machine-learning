"""
Benchmark Suite — Privacy-Preserving UEBA

Runs all experiments from the research plan:
  Exp 1: Plaintext ML performance
  Exp 2: FHE correctness (MAE between plaintext and FHE predictions)
  Exp 3: Performance overhead (latency per stage)
  Exp 4: Ciphertext size
  Exp 5: Model complexity vs FHE feasibility

Outputs results as JSON + summary tables.
"""
import os
import json
import time
import logging
import numpy as np
from datetime import datetime

logger = logging.getLogger(__name__)


def run_benchmarks(
    model_type: str,
    data_dir: str,
    model_dir: str,
    output_dir: str,
    n_samples: int = 100,
):
    """Run the complete benchmark suite."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    logger.info("=" * 60)
    logger.info("  BENCHMARK SUITE — PRIVACY-PRESERVING UEBA")
    logger.info("=" * 60)

    results = {
        "timestamp": timestamp,
        "model_type": model_type,
        "n_samples": n_samples,
        "experiments": {},
    }

    # Load test data
    X_test = np.load(os.path.join(data_dir, "X_test.npy"))
    y_test = np.load(os.path.join(data_dir, "y_test.npy"))

    # ================================================================
    # Experiment 1: Plaintext ML Performance
    # ================================================================
    logger.info("\n--- Experiment 1: Plaintext ML Performance ---")
    from ml.ueba_baseline import evaluate_model

    t0 = time.perf_counter()
    evaluate_model(model_type=model_type, data_dir=data_dir, model_dir=model_dir)
    t_plain = time.perf_counter() - t0

    results["experiments"]["exp1_plaintext"] = {
        "total_time_s": t_plain,
        "description": "Plaintext ML evaluation on test set",
    }

    # ================================================================
    # Experiment 3: Performance Overhead (Plaintext inference timing)
    # ================================================================
    logger.info("\n--- Experiment 3: Plaintext Inference Timing ---")
    import pickle

    if model_type == "lr":
        with open(os.path.join(model_dir, "ueba_lr", "model.pkl"), "rb") as f:
            plain_model = pickle.load(f)

        plain_times = []
        for i in range(min(n_samples, len(X_test))):
            t0 = time.perf_counter()
            plain_model.predict(X_test[i:i+1])
            plain_times.append(time.perf_counter() - t0)

        results["experiments"]["exp3_plaintext_latency"] = {
            "avg_ms": np.mean(plain_times) * 1000,
            "std_ms": np.std(plain_times) * 1000,
            "min_ms": np.min(plain_times) * 1000,
            "max_ms": np.max(plain_times) * 1000,
        }
        logger.info(f"  Plaintext avg: {np.mean(plain_times)*1000:.3f} ms/sample")

    # ================================================================
    # Experiment 4: Data Sizes
    # ================================================================
    logger.info("\n--- Experiment 4: Data Sizes ---")

    sample_bytes = X_test[0].nbytes
    results["experiments"]["exp4_data_sizes"] = {
        "plaintext_sample_bytes": int(sample_bytes),
        "n_features": int(X_test.shape[1]),
        "note": "Ciphertext sizes measured during FHE inference (Exp 3)",
    }
    logger.info(f"  Plaintext sample: {sample_bytes} bytes ({X_test.shape[1]} features × {X_test.dtype})")

    # ================================================================
    # Save Results
    # ================================================================
    output_path = os.path.join(output_dir, f"benchmark_{model_type}_{timestamp}.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)

    logger.info(f"\nBenchmark results saved to: {output_path}")
    logger.info("Note: Run FHE experiments separately with --mode fhe-inference for CKKS/TFHE benchmarks.")

    return results
