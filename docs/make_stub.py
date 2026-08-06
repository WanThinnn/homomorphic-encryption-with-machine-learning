import sys
import inspect

# Đường dẫn tới thư mục chứa openfhe.pyd
sys.path.append("D:/Documents/UIT/FHE/homomorphic-encryption-with-machine-learning/src/lib")

try:
    import openfhe
    print("Import openfhe.pyd thành công!")
except ImportError as e:
    print(f"Lỗi import openfhe: {e}")
    sys.exit(1)

def format_docstring(doc: str, indent: str = "    ") -> list[str]:
    """Làm sạch docstring và định dạng đúng thụt lề cho file .pyi."""
    if not doc:
        return []
    
    lines = doc.strip().splitlines()
    # Nếu docstring ngắn (1 dòng)
    if len(lines) == 1:
        return [f'{indent}"""{lines[0]}"""\n']
    
    # Nếu docstring nhiều dòng
    result = [f'{indent}"""\n']
    for line in lines:
        result.append(f'{indent}{line}\n' if line.strip() else '\n')
    result.append(f'{indent}"""\n')
    return result

def generate_stub():
    out_path = "D:/Documents/UIT/FHE/homomorphic-encryption-with-machine-learning/src/lib/openfhe.pyi"
    lines = [
        "# Auto-generated stub for OpenFHE Python Bindings\n",
        "from typing import Any, List, Dict, Overload, Union\n\n"
    ]

    for name in sorted(dir(openfhe)):
        if name.startswith("__") and name != "__init__":
            continue
        
        try:
            obj = getattr(openfhe, name)
        except Exception:
            continue
        
        # 1. Xử lý Class
        if inspect.isclass(obj):
            lines.append(f"class {name}:\n")
            
            # Docstring của Class
            class_doc = inspect.getdoc(obj)
            if class_doc:
                lines.extend(format_docstring(class_doc, indent="    "))
            
            methods = [m for m in dir(obj) if not m.startswith("__") or m in ("__init__",)]
            if not methods:
                lines.append("    pass\n\n")
                continue

            for m_name in sorted(methods):
                try:
                    m_obj = getattr(obj, m_name, None)
                    lines.append(f"    def {m_name}(self, *args: Any, **kwargs: Any) -> Any:\n")
                    
                    # Rút gọn docstring của method (lấy 10 dòng đầu để tránh trùng lặp rác)
                    m_doc = inspect.getdoc(m_obj)
                    if m_doc and m_doc != class_doc:
                        short_doc = "\n".join(m_doc.strip().splitlines()[:10])
                        lines.extend(format_docstring(short_doc, indent="        "))
                        
                    lines.append("        ...\n\n")
                except Exception:
                    lines.append("        ...\n\n")
            lines.append("\n")
            
        # 2. Xử lý Function tự do
        elif callable(obj):
            lines.append(f"def {name}(*args: Any, **kwargs: Any) -> Any:\n")
            f_doc = inspect.getdoc(obj)
            if f_doc:
                lines.extend(format_docstring(f_doc, indent="    "))
            lines.append("    ...\n\n")

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
        
    print(f"Đã sinh file stub chuẩn format tại: {out_path}")

if __name__ == "__main__":
    generate_stub()