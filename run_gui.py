"""
启动 Streamlit GUI 应用

运行此脚本启动 Materials Studio 自动化助手 Web 界面
"""

import subprocess
import sys
from pathlib import Path

def main():
    """启动 Streamlit 应用"""
    app_path = Path(__file__).parent / "gui" / "app.py"
    
    if not app_path.exists():
        print(f"错误: 找不到应用文件 {app_path}")
        sys.exit(1)
    
    print("=" * 70)
    print("Materials Studio 自动化助手")
    print("=" * 70)
    print(f"\n正在启动 Web 界面...")
    print(f"应用文件: {app_path}")
    print("\n提示:")
    print("  - 浏览器将自动打开")
    print("  - 如果没有自动打开，请访问: http://localhost:8501")
    print("  - 按 Ctrl+C 停止服务")
    print("=" * 70)
    print()
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            str(app_path),
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n\n服务已停止")
    except Exception as e:
        print(f"\n错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

