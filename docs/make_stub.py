import sys
import os
import inspect
import re

# Thêm path chứa openfhe.pyd
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'lib'))
import openfhe

out_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'lib', 'openfhe.pyi')

def clean_type(type_str: str) -> str:
    """Chuyển đổi kiểu C++/pybind11 sang kiểu Python chuẩn."""
    type_str = type_str.replace("openfhe.", "")
    type_str = type_str.replace("typing.SupportsInt | typing.SupportsIndex", "int")
    type_str = type_str.replace("typing.SupportsFloat | typing.SupportsIndex", "float")
    type_str = type_str.replace("collections.abc.Sequence", "List")
    type_str = type_str.replace("NoneType", "None")
    return type_str

def parse_pybind_doc(doc: str, method_name: str, indent: str = "    "):
    """Parse signature từ docstring pybind11 ra mã Python stub chuẩn."""
    if not doc:
        return [f"{indent}def {method_name}(self, *args: Any, **kwargs: Any) -> Any: ...\n\n"]

    lines = doc.strip().splitlines()
    signatures = []
    
    # Tìm các dòng chứa signature: Name(arg1: Type, ...) -> ReturnType
    pattern = re.compile(rf"^\s*(?:\d+\.\s*)?{re.escape(method_name)}\((.*?)\)\s*->\s*(.+)$")

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            args_raw, ret_type = match.groups()
            ret_type = clean_type(ret_type.strip())
            
            # Phân tích từng tham số
            args_list = []
            if args_raw.strip():
                # Tách tham số (tránh ngắt nhầm dấu phẩy nằm trong Union/List)
                raw_params = re.split(r',\s*(?=[a-zA-Z_][a-zA-Z0-9_]*:)', args_raw)
                for param in raw_params:
                    if ':' in param:
                        p_name, p_type = param.split(':', 1)
                        p_name = p_name.strip()
                        
                        # Xử lý default value nếu có
                        if '=' in p_type:
                            p_type_only, default_val = p_type.split('=', 1)
                            p_type = clean_type(p_type_only.strip())
                            args_list.append(f"{p_name}: {p_type} = ...")
                        else:
                            p_type = clean_type(p_type.strip())
                            args_list.append(f"{p_name}: {p_type}")
                    else:
                        args_list.append(param.strip())

            # Chuẩn hóa self/cls
            parsed_args = ", ".join(args_list)
            parsed_args = parsed_args.replace("self: object", "self").replace(f"self: {method_name}", "self")
            
            signatures.append((parsed_args, ret_type))

    if not signatures:
        return [f"{indent}def {method_name}(self, *args: Any, **kwargs: Any) -> Any: ...\n\n"]

    res_lines = []
    # Nếu có nhiều hơn 1 signature -> Dùng @overload
    is_overload = len(signatures) > 1

    for args, ret in signatures:
        if is_overload:
            res_lines.append(f"{indent}@overload\n")
        res_lines.append(f"{indent}def {method_name}({args}) -> {ret}: ...\n")
    
    res_lines.append("\n")
    return res_lines

def generate_stub():
    lines = [
        "# Auto-generated typed stub for OpenFHE\n",
        "from typing import Any, List, Dict, Overload, Union, overload\n\n"
    ]

    for name in sorted(dir(openfhe)):
        if name.startswith("__") and name != "__init__":
            continue
            
        obj = getattr(openfhe, name, None)
        if obj is None:
            continue

        if inspect.isclass(obj):
            lines.append(f"class {name}:\n")
            methods = [m for m in dir(obj) if not m.startswith("__") or m == "__init__"]
            if not methods:
                lines.append("    pass\n\n")
                continue

            for m_name in sorted(methods):
                m_obj = getattr(obj, m_name, None)
                m_doc = inspect.getdoc(m_obj) if m_obj else ""
                lines.extend(parse_pybind_doc(m_doc, m_name, indent="    "))
            lines.append("\n")

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f" Thành công! Đã tạo Stub File có Type Hint chuẩn tại: {out_path}")

if __name__ == "__main__":
    generate_stub()