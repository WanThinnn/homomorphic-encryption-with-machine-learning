"""
Privacy-Preserving UEBA — Unified CLI Entry Point

Supports three modes:
  1. plaintext  — Train/evaluate ML models on plaintext behavioral data
  2. openfhe    — Run FHE inference using OpenFHE (CKKS scheme)
  3. concrete   — Run FHE inference using Concrete ML (TFHE scheme)

Usage:
  python src/main.py --mode train --model lr
  python src/main.py --mode train --model mlp
  python src/main.py --mode evaluate --model lr
  python src/main.py --mode fhe-inference --model lr --platform openfhe
  python src/main.py --mode fhe-inference --model mlp --platform concrete
  python src/main.py --mode benchmark --model lr
"""
import os
import sys
import io
import argparse
import logging

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("UEBA")

# Ensure src/ is on the path
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


def cmd_train(args):
    """Train a Concrete ML model (FHE-native), compile FHE circuit, and save."""
    from ml.ueba_concrete_ml import train_model
    train_model(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        epochs=args.epochs,
    )


def cmd_evaluate(args):
    """Evaluate a trained Concrete ML model on the test set (plaintext simulate)."""
    from ml.ueba_concrete_ml import evaluate_model
    evaluate_model(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
    )


def cmd_fhe_inference(args):
    """Run REAL FHE encrypted inference using a saved compiled model."""
    from ml.ueba_concrete_ml import run_fhe_inference
    run_fhe_inference(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        n_samples=args.n_samples,
    )


def cmd_benchmark(args):
    """Run the full benchmark suite (plaintext vs FHE)."""
    from benchmark.run_all_experiments import run_benchmarks
    run_benchmarks(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        output_dir=os.path.join(ROOT_DIR, "logs"),
        n_samples=args.n_samples,
    )


def cmd_prepare_data(args):
    """Process raw logs into behavioral_features.csv using the appropriate Adapter."""
    from data.cert_preprocessor import preprocess

    raw_dir = os.path.join(ROOT_DIR, "data", "cert", "raw")
    out_dir = os.path.join(ROOT_DIR, "data", "cert", "processed")

    logger.info(f"Step 1: Extracting behavioral features using {args.source.upper()} adapter...")

    if args.source == "cert":
        from data.adapters.cert_adapter import CertAdapter
        # For CERT, check if r4.2 or r5.2 exists
        if os.path.exists(os.path.join(raw_dir, "r4.2")):
            raw_dir = os.path.join(raw_dir, "r4.2")
        adapter = CertAdapter()
    elif args.source == "elastic":
        from data.adapters.elastic_ecs_adapter import ElasticEcsAdapter
        adapter = ElasticEcsAdapter()
    elif args.source == "splunk":
        # Placeholder for Splunk Adapter
        raise NotImplementedError("Splunk adapter is not implemented yet.")
    else:
        raise ValueError(f"Unknown source adapter: {args.source}")

    adapter.extract_features(raw_dir=raw_dir, output_dir=out_dir)

    logger.info("Step 2: Preprocessing (normalize, split, handle imbalance)...")
    preprocess(data_dir=out_dir)

    logger.info("Data preparation complete!")


def main():
    parser = argparse.ArgumentParser(
        description="Privacy-Preserving UEBA with FHE + ML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="mode", help="Operating mode")

    # --- prepare-data ---
    sp_data = subparsers.add_parser("prepare-data", help="Download & process dataset")
    sp_data.add_argument("--source", choices=["cert", "elastic", "splunk"], default="cert", help="Data source adapter to use")

    # --- train ---
    sp_train = subparsers.add_parser("train", help="Train FHE-native model (Concrete ML)")
    sp_train.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_train.add_argument("--epochs", type=int, default=50, help="Training epochs (MLP only)")

    # --- evaluate ---
    sp_eval = subparsers.add_parser("evaluate", help="Evaluate trained model on test set")
    sp_eval.add_argument("--model", choices=["lr", "mlp"], default="lr")

    # --- fhe-inference ---
    sp_fhe = subparsers.add_parser("fhe-inference", help="Run REAL FHE encrypted inference")
    sp_fhe.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_fhe.add_argument("--n-samples", type=int, default=10, help="Number of test samples")

    # --- benchmark ---
    sp_bench = subparsers.add_parser("benchmark", help="Run full benchmark suite")
    sp_bench.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_bench.add_argument("--n-samples", type=int, default=100)

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(0)

    print("=" * 60)
    print("  PRIVACY-PRESERVING UEBA WITH FHE + ML")
    print("=" * 60)

    dispatch = {
        "prepare-data": cmd_prepare_data,
        "train": cmd_train,
        "evaluate": cmd_evaluate,
        "fhe-inference": cmd_fhe_inference,
        "benchmark": cmd_benchmark,
    }
    dispatch[args.mode](args)


if __name__ == "__main__":
    main()
