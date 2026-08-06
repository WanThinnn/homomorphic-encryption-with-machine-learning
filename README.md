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

This project specifically utilizes the CKKS scheme (Cheon-Kim-Kim-Song), which is highly optimized for approximate arithmetic on real and complex numbers, making it the industry standard for privacy-preserving Machine Learning.

## Project Structure and Technologies

The architecture separates the Machine Learning workflow (using standard libraries like Scikit-Learn) from the FHE execution engine.

- Client Side: Uses standard System Python to train models, extract weights (Plaintext), and prepare data (TF-IDF vectorization).
- Server Side / Worker: Utilizes OpenFHE (a leading open-source FHE library written in C++) via Python bindings to execute linear combinations and matrix multiplications entirely on ciphertext.

## Dependencies (src/lib)

To bridge the gap between high-performance C++ lattice cryptography and Python, this project bundles several compiled dynamic link libraries (DLLs) built via MinGW-w64 in the src/lib directory.

### Core OpenFHE Libraries
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
- openfhe.pyd: The PyBind11 compiled wrapper that exposes the underlying C++ OpenFHE classes (like CryptoContext, Ciphertext, and Plaintext) natively to Python.
