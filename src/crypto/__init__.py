"""
Crypto module — Mã hóa đồng cấu FHE (CKKS) và dịch vụ Cross-Tenant (v2).

Components:
- FHEPipeline: Quản lý CryptoContext, tạo khóa, mã hóa/giải mã
- simd_ops: Phép toán SIMD matrix-vector trên CKKS (thay thế element-wise)
- CrossTenantService: Encrypted cross-tenant threat intelligence
"""

from .homomorphic_encryption import FHEPipeline

__all__ = ["FHEPipeline"]
