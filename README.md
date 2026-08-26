# Homomorphic Encryption with Machine Learning

This project serves as an experimental foundation to explore the concepts of Fully Homomorphic Encryption (FHE) and its practical application in Machine Learning and Artificial Intelligence. The primary focus is to build "Blind A.I." systems for the Information Security domain, where sensitive data can be processed and inferred without ever being decrypted in memory.

## Fully Homomorphic Encryption (FHE)

Fully Homomorphic Encryption is a revolutionary cryptographic scheme that allows mathematical operations to be performed directly on ciphertext. Unlike traditional encryption schemes (such as AES or RSA) where data must be decrypted before it can be processed, FHE ensures that data remains encrypted at all stages of computation. 

When the computed ciphertext is eventually decrypted, the result matches the exact output as if the operations had been performed on the original plaintext. This eliminates the need for trusted third parties and solves the privacy paradox in cloud computing.

## FHE in Artificial Intelligence (Blind A.I.)

In the era of Artificial Intelligence, data privacy is a massive concern. Organizations are reluctant to send sensitive information (such as medical records, financial logs, or personal communications) to cloud AI providers. 

By integrating FHE into Machine Learning (ML) and Deep Learning (DL), we can achieve Blind A.I.:
- Privacy-Preserving Inference: A client encrypts their raw data and sends the ciphertext to an AI server. The server runs its ML model (e.g., Logistic Regression, Neural Networks) directly on the encrypted data. The server returns an encrypted prediction, which only the client can decrypt. The server learns nothing about the input data or the result.
- Secure Data Handling: FHE is resistant to quantum computing attacks (lattice-based cryptography) and guarantees that even if the server is compromised or malicious, the underlying data remains mathematically secure.

This project utilizes two state-of-the-art FHE backends:
1. **OpenFHE (CKKS Scheme)**: Highly optimized for approximate arithmetic on real and complex numbers. Used primarily for evaluating linear combinations on encrypted text vectors.
2. **Concrete ML (TFHE Scheme)**: Built by Zama, this scheme supports exact boolean/integer arithmetic and table lookups (Programmable Bootstrapping). It enables fast evaluation of non-linear models like Decision Trees (XGBoost) and Neural Networks on encrypted data using Quantization.

## Project Structure and Technologies

The architecture separates the Machine Learning workflow from the FHE execution engine, offering a unified **Dual-Backend CLI**:

- **Client Side**: Uses standard System Python to prepare data (e.g., TF-IDF vectorization or Quantization) and generate encryption keys.
- **Server Side / Worker**: Runs an isolated subprocess to execute matrix multiplications or non-linear functions entirely on ciphertext, completely blind to the underlying data.

### Dual-Backend Usage
You can run the Blind A.I. pipeline using the unified CLI:
```bash
# Run with OpenFHE backend (CKKS - Linear Models)
python3 src/main.py --model simple_logistic_regression --platform openfhe

# Run with Concrete ML backend (TFHE - Non-linear Models like XGBoost)
python3 src/main.py --model concrete_pretrained --platform concrete
```
*(Note: Concrete ML requires a Linux/WSL environment)*

### 🛡️ Use Case: Network Intrusion Detection (UNSW-NB15)
This project includes a real-world cybersecurity use case: **privacy-preserving network intrusion detection** using the [UNSW-NB15 dataset](https://huggingface.co/datasets/rdpahalavan/UNSW-NB15) from Hugging Face.

**Scenario (SOC Context):** A Security Operations Center (SOC) needs to analyze network traffic flows to detect intrusion attempts. However, the raw network data contains sensitive information (IP addresses, ports, traffic patterns) that must remain confidential. Using FHE, the SOC can outsource the ML inference to a cloud server without exposing any of the actual traffic data.

**Step 1: Train & Compile the Model (Linux/WSL)**
```bash
# Download UNSW-NB15 from HuggingFace, train XGBoost, compile to FHE circuit
python3 src/ml/train_unsw_nb15.py

# Optional: Customize sample size for faster compilation
python3 src/ml/train_unsw_nb15.py --n-samples 5000
```

**Step 2: Run FHE Inference**
```bash
# Run the privacy-preserving intrusion detection pipeline
python3 src/main.py --model unsw_nb15_xgb --platform concrete_ml
```

The model classifies network flows as **Normal** or **Attack** using 49 features (flow statistics, protocol metadata, TCP characteristics, etc.) — all computed entirely on encrypted data.

## Dependencies (src/lib)

To bridge the gap between high-performance C++ lattice cryptography and Python, this project bundles several compiled dynamic link libraries (DLLs) built via MinGW-w64 in the src/lib directory.

### Core OpenFHE Libraries (for CKKS Backend)
- libOPENFHEcore.dll: The foundational module handling lattice parameters, math backends, and serialization.
- libOPENFHEpke.dll: The Public Key Encryption module implementing modern FHE schemes like CKKS, BFV, and BGV.
- libOPENFHEbinfhe.dll: The Boolean FHE module for encrypted boolean logic circuits.

### Math and Cryptography Backends
FHE requires heavy polynomial arithmetic over extremely large integers (often exceeding native 64-bit limits).
- libgmp-10.dll / libgmpxx-4.dll: The GNU Multiple Precision Arithmetic Library (GMP). It provides highly optimized arbitrary-precision arithmetic.
- libntl-45.dll: The Number Theory Library (NTL). A high-performance C++ library for doing number theory, polynomial arithmetic, and lattice-reduction, which acts as the mathematical backbone for OpenFHE's polynomial operations.

### Runtime and Threading
- libgcc_s_seh-1.dll / libstdc++-6.dll: Standard C and C++ runtime libraries required by MinGW-w64 GCC.
- libgomp-1.dll / libwinpthread-1.dll: GNU OpenMP and POSIX thread libraries used to parallelize and accelerate heavy polynomial multiplications across multiple CPU cores.

### Python Bindings
- openfhe.pyd: The PyBind11 compiled wrapper that exposes the underlying C++ OpenFHE classes (like CryptoContext, Ciphertext, and Plaintext) natively to Python on Windows.

## Concrete ML (Zama) Dependency
For the TFHE backend, this project leverages `concrete-ml`, an open-source framework by Zama built on top of `concrete-python` and the `tfhe-rs` Rust compiler. It allows compiling standard Scikit-Learn (e.g., XGBoost, Logistic Regression) and PyTorch models directly into FHE circuits. Because it relies heavily on LLVM and Rust toolchains, it is currently supported exclusively on Linux/WSL environments.
