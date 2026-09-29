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
from typing import Optional

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


def _data_dir(source: str, dataset: str = "default") -> str:
    """Resolve the processed data directory for a given source and dataset version."""
    return os.path.join(ROOT_DIR, "data", source, "processed", dataset)


def _detect_dataset(source: str, dataset: Optional[str] = None) -> str:
    """Auto-detect the dataset version if not specified."""
    if dataset:
        return dataset
    raw_dir = os.path.join(ROOT_DIR, "data", source, "raw")
    if source == "cert":
        # Scan for r*.* directories (e.g., r4.2, r5.2, r6.2)
        if os.path.exists(raw_dir):
            versions = sorted([d for d in os.listdir(raw_dir)
                              if os.path.isdir(os.path.join(raw_dir, d)) and d.startswith("r")],
                             reverse=True)
            if versions:
                return versions[0]  # Latest version (e.g., r5.2 > r4.2)
    # Fallback: check processed directory for any subdirectories
    proc_dir = os.path.join(ROOT_DIR, "data", source, "processed")
    if os.path.exists(proc_dir):
        subs = [d for d in os.listdir(proc_dir) if os.path.isdir(os.path.join(proc_dir, d))]
        if subs:
            return sorted(subs)[-1]
    return "default"


def cmd_train(args):
    """Train a Concrete ML model (FHE-native), compile FHE circuit, and save."""
    from ml.ueba_concrete_ml import train_model
    dataset = _detect_dataset(args.source, args.dataset)
    logger.info(f"Using dataset: {args.source}/{dataset}")
    train_model(
        model_type=args.model,
        data_dir=_data_dir(args.source, dataset),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        epochs=args.epochs,
        source=args.source,
        dataset=dataset,
    )


def cmd_evaluate(args):
    """Evaluate a trained Concrete ML model on the test set (plaintext simulate)."""
    from ml.ueba_concrete_ml import evaluate_model
    dataset = _detect_dataset(args.source, args.dataset)
    evaluate_model(
        model_type=args.model,
        data_dir=_data_dir(args.source, dataset),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        version=args.version,
    )


def cmd_fhe_inference(args):
    """Run REAL FHE encrypted inference using a saved compiled model."""
    from ml.ueba_concrete_ml import run_fhe_inference
    dataset = _detect_dataset(args.source, args.dataset)
    run_fhe_inference(
        model_type=args.model,
        data_dir=_data_dir(args.source, dataset),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        n_samples=args.n_samples,
        version=args.version,
    )


def cmd_benchmark(args):
    """Run the full benchmark suite (plaintext vs FHE)."""
    from benchmark.run_all_experiments import run_benchmarks
    dataset = _detect_dataset(args.source, args.dataset)
    run_benchmarks(
        model_type=args.model,
        data_dir=_data_dir(args.source, dataset),
        model_dir=os.path.join(SRC_DIR, "ml", "models"),
        output_dir=os.path.join(ROOT_DIR, "logs"),
        n_samples=args.n_samples,
    )


def cmd_prepare_data(args):
    """Process raw logs into behavioral_features.csv using the appropriate Adapter."""
    from data.cert_preprocessor import preprocess

    dataset = _detect_dataset(args.source, args.dataset)
    raw_dir = os.path.join(ROOT_DIR, "data", args.source, "raw", dataset)
    out_dir = _data_dir(args.source, dataset)

    logger.info(f"Step 1: Extracting features using {args.source.upper()} adapter (dataset={dataset})...")

    if args.source == "cert":
        from data.adapters.cert_adapter import CertAdapter
        adapter = CertAdapter()
    elif args.source == "elastic":
        from data.adapters.elastic_ecs_adapter import ElasticEcsAdapter
        adapter = ElasticEcsAdapter()
    elif args.source == "splunk":
        raise NotImplementedError("Splunk adapter is not implemented yet.")
    else:
        raise ValueError(f"Unknown source adapter: {args.source}")

    if not os.path.exists(raw_dir):
        logger.error(f"Raw data directory not found: {raw_dir}")
        logger.error(f"Please place your dataset files in: {raw_dir}")
        return

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

    SOURCE_CHOICES = ["cert", "elastic", "splunk"]
    DATASET_HELP = "Dataset version (e.g., r4.2, r5.2, 2024-q1). Auto-detects if not specified."

    # --- prepare-data ---
    sp_data = subparsers.add_parser("prepare-data", help="Download & process dataset")
    sp_data.add_argument("--source", choices=SOURCE_CHOICES, default="cert", help="Data source adapter")
    sp_data.add_argument("--dataset", type=str, default=None, help=DATASET_HELP)

    # --- train ---
    sp_train = subparsers.add_parser("train", help="Train FHE-native model (Concrete ML)")
    sp_train.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_train.add_argument("--epochs", type=int, default=50, help="Training epochs (MLP only)")
    sp_train.add_argument("--source", choices=SOURCE_CHOICES, default="cert", help="Data source")
    sp_train.add_argument("--dataset", type=str, default=None, help=DATASET_HELP)

    # --- evaluate ---
    sp_eval = subparsers.add_parser("evaluate", help="Evaluate trained model on test set")
    sp_eval.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_eval.add_argument("--version", type=int, default=None, help="Model version (default: latest)")
    sp_eval.add_argument("--source", choices=SOURCE_CHOICES, default="cert", help="Data source")
    sp_eval.add_argument("--dataset", type=str, default=None, help=DATASET_HELP)

    # --- fhe-inference ---
    sp_fhe = subparsers.add_parser("fhe-inference", help="Run REAL FHE encrypted inference")
    sp_fhe.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_fhe.add_argument("--n-samples", type=int, default=10, help="Number of test samples")
    sp_fhe.add_argument("--version", type=int, default=None, help="Model version (default: latest)")
    sp_fhe.add_argument("--source", choices=SOURCE_CHOICES, default="cert", help="Data source")
    sp_fhe.add_argument("--dataset", type=str, default=None, help=DATASET_HELP)

    # --- benchmark ---
    sp_bench = subparsers.add_parser("benchmark", help="Run full benchmark suite")
    sp_bench.add_argument("--model", choices=["lr", "mlp"], default="lr")
    sp_bench.add_argument("--n-samples", type=int, default=100)
    sp_bench.add_argument("--source", choices=SOURCE_CHOICES, default="cert", help="Data source")
    sp_bench.add_argument("--dataset", type=str, default=None, help=DATASET_HELP)

    # --- list-versions ---
    sp_versions = subparsers.add_parser("list-versions", help="List all trained model versions")
    sp_versions.add_argument("--model", choices=["lr", "mlp"], default="mlp")

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
        "list-versions": lambda args: __import__('ml.ueba_concrete_ml', fromlist=['list_versions']).list_versions(
            model_dir=os.path.join(SRC_DIR, "ml", "models"),
            model_type=args.model,
        ),
    }
    dispatch[args.mode](args)


if __name__ == "__main__":
    main()
