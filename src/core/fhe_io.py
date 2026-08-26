"""Pack/unpack batched FHE payloads so the worker loads keys/model once."""
import struct
from typing import List, Tuple


def write_blob_list(path: str, blobs: List[bytes]) -> None:
    with open(path, "wb") as f:
        f.write(struct.pack("<I", len(blobs)))
        for blob in blobs:
            f.write(struct.pack("<I", len(blob)))
            f.write(blob)


def read_blob_list(path: str) -> List[bytes]:
    with open(path, "rb") as f:
        (count,) = struct.unpack("<I", f.read(4))
        blobs = []
        for _ in range(count):
            (length,) = struct.unpack("<I", f.read(4))
            blobs.append(f.read(length))
        return blobs


def write_concrete_batch(path: str, eval_keys: bytes, payloads: List[bytes]) -> None:
    with open(path, "wb") as f:
        f.write(struct.pack("<I", len(eval_keys)))
        f.write(eval_keys)
        f.write(struct.pack("<I", len(payloads)))
        for payload in payloads:
            f.write(struct.pack("<I", len(payload)))
            f.write(payload)


def read_concrete_batch(path: str) -> Tuple[bytes, List[bytes]]:
    with open(path, "rb") as f:
        (key_len,) = struct.unpack("<I", f.read(4))
        eval_keys = f.read(key_len)
        (count,) = struct.unpack("<I", f.read(4))
        payloads = []
        for _ in range(count):
            (length,) = struct.unpack("<I", f.read(4))
            payloads.append(f.read(length))
        return eval_keys, payloads
