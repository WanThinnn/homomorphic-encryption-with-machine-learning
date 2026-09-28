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
    """Train a plaintext ML model on CERT behavioral features."""
    from ml.ueba_baseline import train_model
    train_model(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        output_dir=os.path.join(SRC_DIR, "ml", "models"),
        epochs=args.epochs,
    )


def cmd_evaluate(args):
    """Evaluate a trained plaintext model."""
    from ml.ueba_baseline import evaluate_model
    evaluate_model(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
    )


def cmd_fhe_inference(args):
    """Run FHE inference on a single sample or batch."""
    if args.platform == "openfhe":
        from crypto.ueba_ckks_inference import run_ckks_inference
        run_ckks_inference(
            model_type=args.model,
            data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
            model_dir=os.path.join(SRC_DIR, "ml", "models"),
            n_samples=args.n_samples,
        )
    elif args.platform == "concrete":
        from ml.ueba_concrete_ml import run_concrete_inference
        run_concrete_inference(
            model_type=args.model,
            data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
            model_dir=os.path.join(SRC_DIR, "ml", "models"),
            n_samples=args.n_samples,
        )
    else:
        logger.error(f"Unknown platform: {args.platform}")
        sys.exit(1)


def cmd_benchmark(args):
    """Run the full benchmark suite (plaintext vs CKKS vs TFHE)."""
    from benchmark.run_all_experiments import run_benchmarks
    run_benchmarks(
        model_type=args.model,
        data_dir=os.path.join(ROOT_DIR, "data", "cert", "processed"),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        output_dir=os.path.join(ROOT_DIR, "logs"),
        n_samples=args.n_samples,
    )


def cmd_prepare_data(args):
    """Download and process CERT v4.2 dataset."""
    from data.cert_feature_extractor import extract_features
    from data.cert_preprocessor import preprocess

    raw_dir = os.path.join(ROOT_DIR, "data", "cert", "raw")
    if args.dataset_version and os.path.exists(os.path.join(raw_dir, args.dataset_version)):
        raw_dir = os.path.join(raw_dir, args.dataset_version)
    elif os.path.exists(os.path.join(raw_dir, "r4.2")):
        # Default fallback to r4.2 if not specified but exists
        raw_dir = os.path.join(raw_dir, "r4.2")
        
    out_dir = os.path.join(ROOT_DIR, "data", "cert", "processed")

    logger.info("Step 1: Extracting behavioral features from raw CERT logs...")
    extract_features(raw_dir=raw_dir, output_dir=out_dir)

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
    sp_data = subparsers.add_parser("prepare-data", help="Download & process CERT dataset")
    sp_data.add_argument("--dataset-version", type=str, default=None, help="E.g., 'r5.2' to process a specific version folder")

    # --- train ---
    sp_train = subparsers.add_parser("train", help="Train a plaintext ML model")
    sp_train.add_argument("--model", choices=["lr", "mlp", "autoencoder"], default="lr")
    sp_train.add_argument("--epochs", type=int, default=100)

    # --- evaluate ---
    sp_eval = subparsers.add_parser("evaluate", help="Evaluate a trained model")
    sp_eval.add_argument("--model", choices=["lr", "mlp", "autoencoder"], default="lr")

    # --- fhe-inference ---
    sp_fhe = subparsers.add_parser("fhe-inference", help="Run FHE inference")
    sp_fhe.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_fhe.add_argument("--platform", choices=["openfhe", "concrete"], default="openfhe")
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
