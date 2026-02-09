"""
全面测试脚本

测试所有模块的导入和基本功能
"""

import sys
import io

# 设置输出编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("Materials Studio 自动化接口 - 全面测试")
print("=" * 70)

# 测试计数器
tests_passed = 0
tests_failed = 0
errors = []

def test(name, func):
    """运行测试"""
    global tests_passed, tests_failed
    try:
        func()
        print(f"✓ {name}")
        tests_passed += 1
    except Exception as e:
        print(f"✗ {name}: {e}")
        tests_failed += 1
        errors.append((name, str(e)))

# 1. 测试底层模块导入
print("\n1. 测试底层模块 (Driver Layer)")
print("-" * 70)

test("导入 MSComDriver", lambda: __import__('automs.driver.ms_com_driver', fromlist=['MSComDriver']))
test("导入 MSApplication (driver)", lambda: __import__('automs.driver.ms_application', fromlist=['MSApplication']))
test("从 driver 导入", lambda: __import__('automs.driver', fromlist=['MSComDriver', 'MSApplication']))

# 2. 测试中层模块导入
print("\n2. 测试中层模块 (Wrapper Layer)")
print("-" * 70)

test("导入 CalculatorBase", lambda: __import__('automs.wrapper.calculators', fromlist=['CalculatorBase']))
test("导入 ForciteCalculator", lambda: __import__('automs.wrapper.calculators', fromlist=['ForciteCalculator']))
test("导入 CASTEPCalculator", lambda: __import__('automs.wrapper.calculators', fromlist=['CASTEPCalculator']))
test("导入 DMol3Calculator", lambda: __import__('automs.wrapper.calculators', fromlist=['DMol3Calculator']))
test("导入 StructureOperations", lambda: __import__('automs.wrapper.structure_ops', fromlist=['StructureOperations']))
test("从 wrapper 导入", lambda: __import__('automs.wrapper', fromlist=['ForciteCalculator', 'StructureOperations']))

# 3. 测试上层模块导入
print("\n3. 测试上层模块 (Workflow Layer)")
print("-" * 70)

test("导入 BatchCalculator", lambda: __import__('automs.workflow.batch_calculator', fromlist=['BatchCalculator']))
test("导入 ParameterScanner", lambda: __import__('automs.workflow.parameter_scan', fromlist=['ParameterScanner']))
test("导入 ConvergenceTester", lambda: __import__('automs.workflow.convergence_test', fromlist=['ConvergenceTester']))
test("从 workflow 导入", lambda: __import__('automs.workflow', fromlist=['BatchCalculator', 'ParameterScanner']))

# 4. 测试主模块导入
print("\n4. 测试主模块导入")
print("-" * 70)

test("从 automs 导入底层类", lambda: __import__('automs', fromlist=['MSApplication', 'MSComDriver']))
test("从 automs 导入中层类", lambda: __import__('automs', fromlist=['ForciteCalculator', 'StructureOperations']))
test("从 automs 导入上层类", lambda: __import__('automs', fromlist=['BatchCalculator', 'ParameterScanner']))
test("从 automs 导入向后兼容类", lambda: __import__('automs', fromlist=['MaterialsStudio', 'MSStructure', 'MSCalculation']))

# 5. 测试类实例化（不实际连接）
print("\n5. 测试类实例化")
print("-" * 70)

def test_instantiation():
    from automs.driver import MSComDriver, MSApplication
    from automs.wrapper import ForciteCalculator, StructureOperations
    from automs.workflow import BatchCalculator
    
    # 测试底层
    driver = MSComDriver()
    assert driver is not None
    
    app = MSApplication(driver)
    assert app is not None
    
    # 测试中层
    structure_ops = StructureOperations(app)
    assert structure_ops is not None
    
    calculator = ForciteCalculator(app)
    assert calculator is not None
    
    # 测试上层
    batch_calc = BatchCalculator(app)
    assert batch_calc is not None

test("类实例化", test_instantiation)

# 6. 测试工具函数
print("\n6. 测试工具函数")
print("-" * 70)

def test_utils():
    from automs.ms_utils import (
        find_ms_installation,
        get_supported_formats,
        format_energy,
        format_coordinates,
        validate_structure,
        get_structure_info
    )
    
    # 测试函数存在
    assert callable(find_ms_installation)
    assert callable(get_supported_formats)
    assert callable(format_energy)
    assert callable(format_coordinates)
    assert callable(validate_structure)
    assert callable(get_structure_info)
    
    # 测试一些函数
    formats = get_supported_formats()
    assert isinstance(formats, dict)
    
    energy_str = format_energy(1234.567, "eV")
    assert isinstance(energy_str, str)

test("工具函数导入和基本功能", test_utils)

# 7. 测试向后兼容
print("\n7. 测试向后兼容")
print("-" * 70)

def test_backward_compatibility():
    from automs import MaterialsStudio, MSStructure, MSCalculation
    
    # 这些应该是新类的别名
    assert MaterialsStudio is not None
    assert MSStructure is not None
    assert MSCalculation is not None

test("向后兼容接口", test_backward_compatibility)

# 8. 测试模块结构
print("\n8. 测试模块结构")
print("-" * 70)

def test_module_structure():
    import automs
    import automs.driver
    import automs.wrapper
    import automs.workflow
    
    # 检查 __all__
    assert hasattr(automs, '__all__')
    assert hasattr(automs.driver, '__all__')
    assert hasattr(automs.wrapper, '__all__')
    assert hasattr(automs.workflow, '__all__')

test("模块结构完整性", test_module_structure)

# 总结
print("\n" + "=" * 70)
print("测试总结")
print("=" * 70)
print(f"通过: {tests_passed}")
print(f"失败: {tests_failed}")

if errors:
    print("\n错误详情:")
    for name, error in errors:
        print(f"  - {name}: {error}")

if tests_failed == 0:
    print("\n✓ 所有测试通过！")
    sys.exit(0)
else:
    print(f"\n✗ 有 {tests_failed} 个测试失败")
    sys.exit(1)

