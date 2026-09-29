# Privacy-Preserving UEBA with Fully Homomorphic Encryption

Privacy-preserving **User and Entity Behavior Analytics (UEBA)** system that enables enterprises to outsource ML-based cybersecurity analytics to the cloud **without exposing sensitive behavioral data**.

## Overview

```
Enterprise                          Cloud (semi-honest)
┌─────────────────────┐             ┌─────────────────────┐
│ Security Logs       │             │                     │
│       ↓             │             │                     │
│ Feature Extraction  │  ciphertext │                     │
│       ↓             │ ──────────→ │  ML(Enc(x))         │
│ FHE Encrypt(x)      │             │       ↓             │
│                     │ ←────────── │  Enc(score)         │
│ Decrypt → Score     │             │  (never sees x)     │
│       ↓             │             │                     │
│ SOC Decision        │             │                     │
└─────────────────────┘             └─────────────────────┘
```

**Core idea**: ML detects anomalous user behavior, FHE ensures the cloud never sees plaintext behavioral data.

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **FHE Backend 1** | OpenFHE (CKKS) | Approximate arithmetic on real-valued features |
| **FHE Backend 2** | Concrete ML (TFHE) | Quantized ML inference with programmable bootstrapping |
| **ML Models** | Logistic Regression, MLP | Anomaly detection on behavioral vectors |
| **Dataset** | CERT Insider Threat v4.2 | 1000 users, 17 months of security telemetry |
| **Features** | 17 behavioral features | Per-user-per-day aggregated from security logs |

## Project Structure

```
src/
├── main.py                          # Unified CLI entry point
├── data/
│   ├── cert_feature_extractor.py    # Raw CERT logs → behavioral vectors
│   └── cert_preprocessor.py         # Normalize, split, SMOTE
├── ml/
│   ├── ueba_baseline.py             # Plaintext LR + MLP training
│   └── ueba_concrete_ml.py          # Concrete ML (TFHE) pipeline
├── crypto/
│   ├── homomorphic_encryption.py    # OpenFHE CKKS wrapper
│   └── ueba_ckks_inference.py       # CKKS inference for UEBA
├── benchmark/
│   └── run_all_experiments.py       # Full benchmark suite
├── core/
│   └── fhe_io.py                    # FHE serialization utilities
└── lib/
    └── openfhe.pyd                  # OpenFHE Python bindings (Windows)
```

## Quick Start

### 1. Prepare Data
Download CERT v4.2 from [KiltHub](https://doi.org/10.1184/R1/12841247.v1) and extract CSVs to `data/cert/raw/`.

```bash
python src/main.py prepare-data
```

### 2. Train Plaintext Baseline
```bash
# Logistic Regression
python src/main.py train --model lr

# MLP with square activation (FHE-friendly)
python src/main.py train --model mlp --epochs 100
```

### 3. Evaluate
```bash
python src/main.py evaluate --model lr
python src/main.py evaluate --model mlp
```

### 4. FHE Inference
```bash
# CKKS (OpenFHE) — works on Windows
python src/main.py fhe-inference --model lr --platform openfhe --n-samples 10

# TFHE (Concrete ML) — requires Linux/WSL
python src/main.py fhe-inference --model lr --platform concrete --n-samples 10
```

### 5. Benchmark
```bash
python src/main.py benchmark --model lr --n-samples 100
```

## Behavioral Features (17 dimensions)

| # | Feature | Source |
|---|---------|--------|
| 1 | login_count | logon.csv |
| 2 | logoff_count | logon.csv |
| 3 | after_hours_login | logon.csv |
| 4 | unique_machines | logon.csv |
| 5 | file_copy_count | file.csv |
| 6 | file_write_count | file.csv |
| 7 | file_delete_count | file.csv |
| 8 | file_exe_count | file.csv |
| 9 | email_sent | email.csv |
| 10 | email_external | email.csv |
| 11 | email_attachments | email.csv |
| 12 | email_bcc_count | email.csv |
| 13 | usb_connect | device.csv |
| 14 | usb_disconnect | device.csv |
| 15 | http_requests | http.csv |
| 16 | unique_urls | http.csv |
| 17 | unique_domains | http.csv |

## FHE Backends

### OpenFHE (CKKS)
- Approximate arithmetic on encrypted real numbers
- Manual weight encoding and homomorphic inference
- Lower latency for simple models (LR: ~50-200ms/sample)
- Requires `openfhe.pyd` (bundled in `src/lib/`)

### Concrete ML (TFHE)
- Automatic model compilation to FHE circuits
- Supports scikit-learn and PyTorch models
- Programmable bootstrapping (no depth limit)
- **Linux/WSL only**: `pip install concrete-ml`

## Dependencies

You can install the core data science dependencies using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Core requirements include:** `numpy`, `pandas`, `scikit-learn`, `torch`, `imbalanced-learn`.

### FHE Backends Setup

#### 1. Concrete ML (Linux/WSL only - Recommended for TFHE)
To use Concrete ML, you must be on a Linux or WSL environment. 

**For CPU-only inference:**
```bash
pip install concrete-ml==1.9.0
```

**For GPU-accelerated inference (CUDA 11.8+):**
If you have an NVIDIA GPU, you can massively speed up FHE compilation and inference (e.g., from 3 minutes down to milliseconds) by installing the CUDA wheel from Zama's private registry:
```bash
pip install concrete-ml==1.9.0
pip uninstall -y concrete-python concrete-compiler
pip install concrete-python==2.10.0 --extra-index-url https://pypi.zama.ai/gpu
```
*(Make sure the version of `concrete-python` matches exactly what `concrete-ml` requires, here `2.10.0` for `concrete-ml 1.9.0`).*

#### 2. OpenFHE (Windows compatible - CKKS)
Pre-compiled OpenFHE bindings for Python (`openfhe.pyd`) are bundled in the `src/lib/` folder. No external `pip` installation is required if you are on Windows, but you must ensure Python can load `.pyd` files.

## Legacy Code

Previous project code (UNSW-NB15 IDS, text classification, Suricata parser) has been moved to `tmp/legacy_src/` for reference.
