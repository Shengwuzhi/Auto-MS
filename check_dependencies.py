"""
检查依赖安装情况
"""

import sys
import io

# 设置输出编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def check_dependency(module_name, package_name=None, optional=False):
    """检查依赖是否安装"""
    try:
        module = __import__(module_name)
        version = getattr(module, '__version__', '已安装')
        status = "✓"
        print(f"{status} {package_name or module_name}: {version}")
        return True
    except ImportError:
        status = "⚠" if optional else "✗"
        print(f"{status} {package_name or module_name}: 未安装{'（可选）' if optional else ''}")
        return optional

print("=" * 70)
print("依赖检查")
print("=" * 70)

# 必需依赖
print("\n必需依赖:")
required = []
required.append(check_dependency("streamlit", "Streamlit"))
required.append(check_dependency("requests", "Requests"))
required.append(check_dependency("numpy", "NumPy"))
required.append(check_dependency("pandas", "Pandas"))
required.append(check_dependency("matplotlib", "Matplotlib"))
required.append(check_dependency("win32com.client", "pywin32"))

# 可选依赖
print("\n可选依赖（LLM 支持）:")
optional = []
optional.append(check_dependency("openai", "OpenAI", optional=True))
optional.append(check_dependency("google.generativeai", "Google Generative AI", optional=True))

print("\n" + "=" * 70)
if all(required):
    print("✓ 所有必需依赖已安装！")
    if any(optional):
        print("✓ 部分可选依赖已安装（LLM 功能可用）")
    else:
        print("⚠ 可选依赖未安装（LLM 功能不可用，可使用本地模拟模式）")
    print("\n可以运行: python run_gui.py")
else:
    print("✗ 部分必需依赖未安装")
    print("\n请运行: pip install -r requirements.txt")
print("=" * 70)

