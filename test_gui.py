"""
测试 GUI 功能

检查 GUI 模块是否能正常工作
"""

import sys
import io
from pathlib import Path

# 设置输出编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("GUI 功能测试")
print("=" * 70)

# 测试 1: 模块导入
print("\n1. 测试模块导入...")
try:
    sys.path.insert(0, str(Path(__file__).parent))
    from gui.llm_translator import LLMTranslator
    from gui.executor import TaskExecutor
    from gui.visualizer import StructureVisualizer
    print("   ✓ 所有 GUI 模块导入成功")
except Exception as e:
    print(f"   ✗ 导入失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 测试 2: LLM 翻译器
print("\n2. 测试 LLM 翻译器...")
try:
    translator = LLMTranslator(provider="本地模拟")
    test_input = "优化水分子结构，使用 Forcite 计算"
    plan = translator.translate(test_input)
    if plan:
        print(f"   ✓ 翻译成功")
        print(f"   输入: {test_input}")
        print(f"   输出: {plan}")
    else:
        print("   ✗ 翻译返回 None")
except Exception as e:
    print(f"   ✗ 翻译失败: {e}")
    import traceback
    traceback.print_exc()

# 测试 3: 执行器（不实际连接 MS）
print("\n3. 测试执行器初始化...")
try:
    # 不实际连接，只测试类能否初始化
    from automs.driver import MSApplication
    app = MSApplication()
    executor = TaskExecutor(app)
    print("   ✓ 执行器初始化成功")
except Exception as e:
    print(f"   ✗ 执行器初始化失败: {e}")
    import traceback
    traceback.print_exc()

# 测试 4: 可视化器
print("\n4. 测试可视化器...")
try:
    visualizer = StructureVisualizer()
    print("   ✓ 可视化器初始化成功")
except Exception as e:
    print(f"   ✗ 可视化器初始化失败: {e}")
    import traceback
    traceback.print_exc()

# 测试 5: 检查 Streamlit 应用语法
print("\n5. 检查 Streamlit 应用语法...")
try:
    import ast
    app_file = Path(__file__).parent / "gui" / "app.py"
    with open(app_file, 'r', encoding='utf-8') as f:
        code = f.read()
    ast.parse(code)
    print("   ✓ 应用文件语法正确")
except SyntaxError as e:
    print(f"   ✗ 语法错误: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"   ✗ 检查失败: {e}")

print("\n" + "=" * 70)
print("测试完成！")
print("=" * 70)
print("\n如果所有测试通过，可以运行:")
print("  python run_gui.py")
print("\n或者:")
print("  streamlit run gui/app.py")

