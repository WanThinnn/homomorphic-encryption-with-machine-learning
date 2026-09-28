# Privacy-Preserving UEBA using FHE + ML — Optimized Plan

> **Đề tài**: Privacy-Preserving User and Entity Behavior Analytics using Fully Homomorphic Encryption and Machine Learning
>
> **Một dòng tóm tắt**: Enterprise outsource phân tích hành vi user lên cloud bằng ML, FHE đảm bảo cloud không nhìn thấy dữ liệu behavioral plaintext.

---

## 1. Problem Statement

### 1.1. Bài toán
Doanh nghiệp thu thập **security telemetry** (login, file access, email, USB, HTTP...) để phát hiện hành vi bất thường của nhân viên. ML phân tích các **behavioral vectors** đa chiều để scoring anomaly — việc mà rule-based không làm tốt.

### 1.2. Vấn đề privacy
Behavioral data chứa thông tin cực nhạy cảm (ai login ở đâu, truy cập file gì, download bao nhiêu GB). Khi outsource lên cloud → cloud nhìn thấy hết.

### 1.3. Giải pháp
FHE cho phép cloud chạy ML inference trên **ciphertext** → trả về **encrypted score** → chỉ enterprise mới decrypt được.

```text
Enterprise                          Cloud (semi-honest)
┌─────────────────────┐             ┌─────────────────────┐
│ Security Logs       │             │                     │
│       ↓             │             │                     │
│ Feature Extraction  │             │                     │
│       ↓             │  ciphertext │                     │
│ Behavioral Vector   │ ──────────→ │  ML(Enc(x))         │
│       ↓             │             │       ↓             │
│ FHE Encrypt(x)      │             │  Enc(score)         │
│                     │ ←────────── │                     │
│ Decrypt → Score     │             │  (never sees x)     │
│       ↓             │             │                     │
│ SOC Decision        │             │                     │
└─────────────────────┘             └─────────────────────┘
```

---

## 2. Threat Model

| Entity | Trust Level | Capability |
|--------|------------|------------|
| **Enterprise** | Trusted | Giữ secret key, thực hiện feature extraction, encrypt/decrypt |
| **Cloud** | Semi-honest | Thực hiện đúng protocol, có thể observe ciphertext, KHÔNG có secret key |

**Bảo vệ**: User identity, behavioral features, security telemetry, internal infrastructure info.

**KHÔNG giải quyết** (→ Future Work): Malicious cloud, data poisoning, side-channel attacks, model inversion.

---

## 3. Research Questions

| # | Research Question |
|---|---|
| **Main** | Can FHE enable privacy-preserving outsourcing of ML-based UEBA while maintaining acceptable detection performance? |
| **RQ1** | How much detection accuracy is lost when UEBA inference runs on encrypted data vs plaintext? |
| **RQ2** | What is the computational overhead (latency, memory, ciphertext size) of FHE-based UEBA inference? |
| **RQ3** | Which FHE scheme (CKKS vs TFHE) is more suitable for UEBA workloads? |
| **RQ4** | How do model complexity and multiplicative depth affect FHE inference feasibility? |

---

## 4. Dataset

### 4.1. Primary: CERT Insider Threat Dataset v4.2

| Property | Detail |
|----------|--------|
| **Source** | CMU KiltHub — [https://doi.org/10.1184/R1/12841247.v1](https://doi.org/10.1184/R1/12841247.v1) |
| **License** | CC BY 4.0 (free) |
| **Scale** | ~1,000 users, 17 tháng |
| **Format** | CSV files |
| **Ground truth** | Có — `answers.tar.bz2` chứa malicious labels |

**Raw log streams:**

| File | Nội dung |
|------|----------|
| `logon.csv` | Logon/logoff events, timestamps, user/machine IDs |
| `file.csv` | File read/write/copy/delete |
| `email.csv` | Email activity (to, cc, bcc, attachments) |
| `device.csv` | USB/removable device usage |
| `http.csv` | Web browsing activity |

### 4.2. Secondary (Optional): LANL Unified Host and Network Dataset

| Property | Detail |
|----------|--------|
| **Source** | [https://csr.lanl.gov/data/2017.html](https://csr.lanl.gov/data/2017.html) |
| **Scale** | 90 ngày, enterprise network |
| **Streams** | Netflow + Host events (WLS) |
| **Labels** | Chủ yếu normal → cần unsupervised/anomaly detection |

> [!TIP]
> **Khuyến nghị**: Bắt đầu với CERT v4.2 vì có **ground truth labels** rõ ràng → dễ evaluate. LANL dùng để validate nếu còn thời gian.

---

## 5. Feature Engineering

Feature extraction chạy **hoàn toàn ở phía Enterprise** (trước khi encrypt). Mỗi user được aggregate theo **time window** (daily).

### 5.1. Behavioral Feature Vector

Từ raw logs CERT, extract **15–20 features** cho mỗi (user, day):

```python
behavioral_vector = {
    # Logon behavior
    "login_count":           int,    # Số lần logon trong ngày
    "logoff_count":          int,    # Số lần logoff
    "after_hours_login":     int,    # Login ngoài giờ (18:00-06:00)
    "unique_machines":       int,    # Số máy khác nhau đã login

    # File activity
    "file_copy_count":       int,    # Số file copy
    "file_write_count":      int,    # Số file write
    "file_delete_count":     int,    # Số file delete
    "file_exe_count":        int,    # Số file .exe truy cập

    # Email activity
    "email_sent":            int,    # Số email gửi
    "email_external":        int,    # Email gửi ra ngoài org
    "email_attachments":     int,    # Số attachments
    "email_bcc_count":       int,    # Số email có BCC

    # Device activity
    "usb_connect":           int,    # Số lần gắn USB
    "usb_disconnect":        int,    # Số lần rút USB

    # HTTP activity
    "http_requests":         int,    # Số HTTP requests
    "unique_urls":           int,    # Số URL khác nhau
    "unique_domains":        int,    # Số domain khác nhau
}
```

### 5.2. Normalization

```text
Raw features → StandardScaler (z-score) hoặc MinMaxScaler [0,1]
```

> [!IMPORTANT]
> **CKKS** hoạt động tốt hơn với values trong range nhỏ → **MinMaxScaler [0,1]** hoặc **[-1,1]** được khuyến nghị.
> **TFHE (Concrete ML)** tự quantize → StandardScaler OK.

### 5.3. Labeling Strategy

Từ `answers.tar.bz2` của CERT:
- Map malicious user + date → label = 1 (anomalous)
- Còn lại → label = 0 (normal)
- **Class imbalance**: ~99% normal, ~1% malicious

**Xử lý imbalance:**
- SMOTE hoặc ADASYN cho oversampling
- Class weights trong model training
- Evaluation bằng PR-AUC thay vì accuracy (vì accuracy misleading khi imbalance)

---

## 6. Model Architecture

### 6.1. Strategy: 3 tầng phức tạp tăng dần

```text
Level 1: Logistic Regression    → FHE baseline (CKKS native)
Level 2: MLP (2-layer)          → FHE main model (CKKS + Concrete ML)
Level 3: Autoencoder            → FHE stretch goal (nếu đủ thời gian)
```

### 6.2. Model 1 — Logistic Regression (Baseline)

```text
Input(17) → Linear(1) → Sigmoid → Score
```

- **FHE compatibility**: ⭐⭐⭐⭐⭐ — chỉ cần 1 phép nhân + polynomial approximation cho sigmoid
- **Sigmoid approximation**: $\sigma(x) \approx 0.5 + 0.197x - 0.004x^3$ (degree-3 polynomial)
- **Multiplicative depth**: 1–2

### 6.3. Model 2 — MLP (Main Model)

```text
Input(17)
  ↓
Dense(32) → Square activation (x²)
  ↓
Dense(16) → Square activation (x²)
  ↓
Dense(1) → (Output = anomaly score)
```

- **FHE compatibility**: ⭐⭐⭐⭐ — polynomial activations thay thế ReLU
- **Tại sao square (x²)?** Degree thấp nhất, multiplicative depth chỉ tăng 1 per layer
- **Multiplicative depth**: ~4–6
- **Alternative activation**: $f(x) = x^2 + x$ (degree-2, slightly more expressive)

> [!WARNING]
> **KHÔNG dùng ReLU hay Sigmoid trực tiếp** — chúng không phải polynomials → không compute được trên CKKS. Phải dùng polynomial approximation.

### 6.4. Model 3 — Autoencoder (Stretch Goal)

```text
Encoder:  Input(17) → Dense(12) → Dense(8) → Latent(4)
Decoder:  Latent(4) → Dense(8) → Dense(12) → Output(17)

Anomaly Score = MSE(input, output) = ||x - x̂||²
```

- **FHE compatibility**: ⭐⭐ — multiplicative depth cao (~8–12)
- **Chỉ chạy nếu**: MLP đã hoạt động ổn trên FHE
- **Ưu điểm**: Unsupervised, không cần labels

---

## 7. FHE Implementation

### 7.1. Dual-Backend Strategy

Tận dụng cả 2 backend **đã có sẵn** trong project:

| Backend | FHE Scheme | Phù hợp cho | Có sẵn |
|---------|-----------|-------------|--------|
| **OpenFHE** (CKKS) | Approximate arithmetic | Logistic Regression, MLP | ✅ `src/crypto/homomorphic_encryption.py` |
| **Concrete ML** (TFHE) | Quantized integer | MLP, XGBoost, Decision Tree | ✅ `src/ml/concrete_pretrained.py` |

### 7.2. CKKS Pipeline (OpenFHE)

```text
Step 1: Train model on plaintext (scikit-learn / PyTorch)
Step 2: Export weights (W₁, b₁, W₂, b₂, ...)
Step 3: Encrypt input vector → CKKS ciphertext
Step 4: Homomorphic inference:
         Enc(x) → Enc(W₁·x + b₁) → Enc(act(z₁)) → ... → Enc(score)
Step 5: Decrypt → anomaly score
```

**Key parameters (CKKS):**

| Parameter | Recommended Value | Rationale |
|-----------|------------------|-----------|
| Security level | 128-bit | Standard |
| Polynomial degree (N) | 8192 hoặc 16384 | 8192 cho LR, 16384 cho MLP |
| Scale (Δ) | 2⁴⁰ | Đủ precision cho behavioral features |
| Multiplicative depth | 2 (LR) / 6 (MLP) | Tối thiểu cần thiết |
| Batch size | Up to N/2 slots | SIMD packing |

### 7.3. TFHE Pipeline (Concrete ML)

```text
Step 1: Train model on plaintext (scikit-learn / PyTorch)
Step 2: Concrete ML auto-quantizes model
Step 3: Compile to FHE circuit
Step 4: Encrypt input → TFHE ciphertext
Step 5: Run compiled FHE circuit
Step 6: Decrypt → anomaly score
```

**Concrete ML handles:**
- Quantization (automatic)
- FHE circuit compilation
- Key generation
- Programmable bootstrapping (no depth limit)

```python
# Concrete ML example (pseudo-code)
from concrete.ml.sklearn import LogisticRegression, NeuralNetClassifier

# Train
model = NeuralNetClassifier(module__n_layers=2, module__n_hidden=32)
model.fit(X_train, y_train)

# Compile to FHE
model.compile(X_train)

# FHE inference
fhe_circuit = model.fhe_circuit
encrypted_result = fhe_circuit.encrypt_run_decrypt(X_test[0])
```

### 7.4. So sánh CKKS vs TFHE

| Dimension | CKKS (OpenFHE) | TFHE (Concrete ML) |
|-----------|---------------|-------------------|
| Arithmetic | Approximate (floating-point) | Exact (quantized integer) |
| Activation functions | Polynomial approximation | Lookup tables (PBS) |
| Depth limit | Limited by modulus chain | Unlimited (bootstrapping) |
| Implementation effort | **Cao** — manual weight encoding | **Thấp** — auto-compile |
| Latency (LR, 17 features) | ~50–200ms | ~1–5s |
| Latency (MLP 2-layer) | ~1–10s | ~10–60s |
| Precision | Higher (approximate real) | Lower (quantized) |
| Control | Full manual control | Black-box compiler |

---

## 8. Experiments

### Experiment 1 — Plaintext ML Baseline

| Item | Detail |
|------|--------|
| **Goal** | Establish upper-bound performance |
| **Models** | LR, MLP, Autoencoder |
| **Metrics** | Accuracy, Precision, Recall, F1, PR-AUC, ROC-AUC |
| **Data split** | 70/15/15 (train/val/test) |

### Experiment 2 — FHE Correctness

| Item | Detail |
|------|--------|
| **Goal** | Verify $\text{Dec}(\text{ML}(\text{Enc}(x))) \approx \text{ML}(x)$ |
| **Metric** | $\text{MAE} = \frac{1}{n}\sum|y_{\text{plain}} - y_{\text{FHE}}|$ |
| **Expectation** | MAE < 0.01 cho CKKS, exact cho TFHE |

### Experiment 3 — Performance Overhead

| Metric | Plain | CKKS | TFHE |
|--------|-------|------|------|
| Key generation (ms) | - | ✓ | ✓ |
| Encryption (ms/sample) | - | ✓ | ✓ |
| Inference (ms/sample) | ✓ | ✓ | ✓ |
| Decryption (ms/sample) | - | ✓ | ✓ |
| Total E2E (ms/sample) | ✓ | ✓ | ✓ |
| Memory (MB) | ✓ | ✓ | ✓ |

### Experiment 4 — Ciphertext Size

| Metric | Plain | CKKS | TFHE |
|--------|-------|------|------|
| Input size (bytes) | ✓ | ✓ | ✓ |
| Output size (bytes) | ✓ | ✓ | ✓ |
| Expansion ratio | 1x | ? | ? |

### Experiment 5 — Model Complexity vs FHE Feasibility

| Model | Depth | CKKS Feasible | TFHE Feasible | Detection Loss |
|-------|-------|--------------|--------------|---------------|
| LR | 1–2 | ✓ | ✓ | ? |
| MLP-small (32→16→1) | 4–6 | ✓ | ✓ | ? |
| MLP-large (64→32→16→1) | 6–8 | ? | ✓ | ? |
| Autoencoder | 8–12 | Unlikely | ? | ? |

---

## 9. Evaluation Matrix (Complete)

| Metric | Plain-LR | Plain-MLP | CKKS-LR | CKKS-MLP | TFHE-LR | TFHE-MLP |
|--------|----------|-----------|---------|----------|---------|----------|
| Accuracy | | | | | | |
| Precision | | | | | | |
| Recall | | | | | | |
| F1 | | | | | | |
| PR-AUC | | | | | | |
| ROC-AUC | | | | | | |
| Inference (ms) | | | | | | |
| Encrypt (ms) | | | | | | |
| Decrypt (ms) | | | | | | |
| Memory (MB) | | | | | | |
| Ciphertext (KB) | | | | | | |

---

## 10. Development Roadmap

### Phase 1 — Dataset & EDA (Week 1–2)

```text
Deliverables:
  ├── Download CERT v4.2
  ├── EDA notebook (distributions, correlations, class balance)
  ├── Data quality report
  └── Final feature list
```

**Cụ thể làm:**
- [ ] Download CERT v4.2 từ KiltHub
- [ ] Parse `logon.csv`, `file.csv`, `email.csv`, `device.csv`, `http.csv`
- [ ] Parse `answers.tar.bz2` → malicious labels
- [ ] EDA: distribution từng feature, correlation matrix, class ratio
- [ ] Quyết định time window (daily vs weekly)
- [ ] Output: `data/cert/processed/behavioral_features.csv`

---

### Phase 2 — Feature Engineering (Week 2–3)

```text
Deliverables:
  ├── Feature extraction pipeline
  ├── Normalized dataset
  ├── Train/val/test splits
  └── Class imbalance handling
```

**Cụ thể làm:**
- [ ] Implement `src/data/cert_feature_extractor.py`
- [ ] Aggregate raw events → per-user-per-day behavioral vectors
- [ ] Normalize (MinMaxScaler cho CKKS, StandardScaler cho TFHE)
- [ ] Handle imbalance (SMOTE / class weights)
- [ ] Split: 70/15/15
- [ ] Output: `data/cert/processed/X_train.npy`, `y_train.npy`, etc.

---

### Phase 3 — Plaintext ML Baseline (Week 3–4)

```text
Deliverables:
  ├── Trained LR model + metrics
  ├── Trained MLP model + metrics
  ├── Comparison table
  └── Exported model weights
```

**Cụ thể làm:**
- [ ] Implement `src/ml/ueba_baseline.py`
- [ ] Train Logistic Regression (scikit-learn)
- [ ] Train MLP (PyTorch: 17→32→16→1, square activation)
- [ ] Evaluate: Accuracy, Precision, Recall, F1, PR-AUC, ROC-AUC
- [ ] Export weights: `src/ml/models/ueba_lr_weights.npz`, `ueba_mlp_weights.pt`
- [ ] **Gate**: Nếu ML performance quá thấp → revisit features trước khi tiếp

---

### Phase 4 — FHE Integration: CKKS (Week 5–7)

```text
Deliverables:
  ├── CKKS-LR inference working
  ├── CKKS-MLP inference working
  ├── Correctness verification (MAE)
  └── Performance benchmarks
```

**Cụ thể làm:**
- [ ] Implement `src/crypto/ueba_ckks_inference.py`
- [ ] CKKS encrypt behavioral vector
- [ ] Implement homomorphic matrix multiplication (W·Enc(x) + b)
- [ ] Implement polynomial activation on ciphertext
- [ ] Verify: $|y_{\text{plain}} - y_{\text{CKKS}}| < 0.01$
- [ ] Benchmark: keygen, encrypt, inference, decrypt time
- [ ] Measure: ciphertext size, memory usage

---

### Phase 5 — FHE Integration: Concrete ML / TFHE (Week 7–9)

```text
Deliverables:
  ├── TFHE-LR inference working
  ├── TFHE-MLP inference working
  ├── Correctness verification
  └── Performance benchmarks
```

**Cụ thể làm:**
- [ ] Implement `src/ml/ueba_concrete_ml.py`
- [ ] Compile LR to FHE circuit (Concrete ML)
- [ ] Compile MLP to FHE circuit (NeuralNetClassifier)
- [ ] Run `encrypt_run_decrypt` trên test set
- [ ] Benchmark tương tự Phase 4
- [ ] **Chạy trên WSL/Linux** (Concrete ML requirement)

---

### Phase 6 — Comparative Benchmark (Week 9–10)

```text
Deliverables:
  ├── Complete evaluation matrix (filled)
  ├── CKKS vs TFHE comparison
  ├── Charts & visualizations
  └── Analysis report
```

**Cụ thể làm:**
- [ ] Implement `src/benchmark/run_all_experiments.py`
- [ ] Fill toàn bộ evaluation matrix (Section 9)
- [ ] Generate charts:
  - Accuracy comparison bar chart
  - Latency comparison (log scale)
  - Ciphertext expansion ratio
  - Privacy-Performance trade-off plot
- [ ] Write analysis cho từng RQ

---

### Phase 7 — Documentation & Paper (Week 10–12)

```text
Deliverables:
  ├── Final report / paper
  ├── Updated README
  ├── Demo notebook
  └── Reproducibility instructions
```

---

## 11. Project Structure (Target)

```text
homomorphic-encryption-with-machine-learning/
├── src/
│   ├── main.py                          # CLI entry point (updated)
│   ├── data/
│   │   ├── cert_downloader.py           # Download CERT v4.2
│   │   ├── cert_feature_extractor.py    # Raw logs → behavioral vectors
│   │   └── cert_preprocessor.py         # Normalize, split, SMOTE
│   ├── ml/
│   │   ├── ueba_baseline.py             # Train plaintext LR + MLP
│   │   ├── ueba_concrete_ml.py          # Concrete ML (TFHE) pipeline
│   │   ├── models/
│   │   │   ├── ueba_lr_weights.npz
│   │   │   └── ueba_mlp_weights.pt
│   │   └── [existing files...]
│   ├── crypto/
│   │   ├── homomorphic_encryption.py    # [existing] OpenFHE CKKS wrapper
│   │   ├── ueba_ckks_inference.py       # CKKS inference for UEBA
│   │   └── __init__.py
│   ├── benchmark/
│   │   ├── run_all_experiments.py       # Run all experiments
│   │   ├── metrics.py                   # Evaluation metrics
│   │   └── visualize.py                 # Charts & plots
│   └── core/
│       └── [existing files...]
├── data/
│   ├── cert/
│   │   ├── raw/                         # Raw CERT CSV files
│   │   └── processed/                   # Feature vectors, splits
│   └── huggingface/                     # [existing]
├── logs/                                # Experiment logs
├── docs/                                # Documentation
└── README.md                            # Updated
```

---

## 12. Expected Contributions

| # | Contribution |
|---|---|
| **C1** | Architecture cho privacy-preserving UEBA outsourcing sử dụng FHE |
| **C2** | Feature engineering pipeline phù hợp FHE cho cybersecurity behavioral data |
| **C3** | Đánh giá thực nghiệm ML inference trên encrypted UEBA data |
| **C4** | Comparative analysis: CKKS vs TFHE cho cybersecurity ML workloads |
| **C5** | Phân tích trade-off: Privacy ↔ Accuracy ↔ Latency ↔ Resource |

---

## 13. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| CERT dataset khó parse | 🟡 Medium | 🟡 | Có nhiều papers đã dùng, tham khảo code |
| Class imbalance quá lớn | 🟢 High | 🟡 | SMOTE + class weights + PR-AUC thay accuracy |
| CKKS MLP multiplicative depth quá cao | 🟡 Medium | 🔴 | Giảm layers, dùng model nhỏ hơn |
| Concrete ML compile timeout | 🟡 Medium | 🟡 | Giảm quantization bits, giảm model size |
| ML performance thấp (plaintext) | 🟡 Medium | 🔴 | **Gate ở Phase 3** — revisit features trước khi FHE |

---

## 14. Checklist: 6 Decision Gates ✅

Trước khi code, đảm bảo trả lời được:

- [x] **What is the cybersecurity problem?** → User behavioral anomaly detection (UEBA)
- [x] **Why is ML needed?** → Multi-dimensional behavioral patterns không thể detect bằng rules đơn giản
- [x] **Why is the data sensitive?** → Behavioral telemetry tiết lộ identity, habits, internal infrastructure
- [x] **Why outsource to cloud?** → Enterprise cần computational resources / centralized analytics
- [x] **Why is conventional encryption insufficient?** → Cloud phải decrypt để chạy ML
- [x] **Why FHE?** → Cho phép ML inference trên encrypted behavioral vectors mà cloud không cần decrypt

---

## 15. Hypothesis

> **FHE enables privacy-preserving UEBA inference with minimal detection accuracy loss (<5%), but introduces significant computational overhead (10–1000x latency) compared to plaintext inference. The trade-off is justifiable for high-sensitivity environments where behavioral data confidentiality is critical.**

Nghiên cứu sẽ **quantify chính xác** accuracy loss và overhead này.
