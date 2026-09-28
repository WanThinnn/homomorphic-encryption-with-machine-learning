"""
Crypto module — Fully Homomorphic Encryption backends.

Components:
  - FHEPipeline: CKKS scheme via OpenFHE (encrypt, decrypt, eval ops)
  - ueba_ckks_inference: Privacy-preserving UEBA inference over CKKS
"""

from .homomorphic_encryption import FHEPipeline

__all__ = ["FHEPipeline"]
