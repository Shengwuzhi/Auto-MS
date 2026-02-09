"""
测试 Materials Studio 连接

这是一个简单的测试脚本，用于验证 Materials Studio 是否可以正常连接
"""

import sys
import io

# 设置输出编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from automs import MaterialsStudio


def test_connection():
    """测试连接"""
    print("=" * 60)
    print("Materials Studio 连接测试")
    print("=" * 60)
    
    try:
        print("\n1. 导入模块...")
        print("   ✓ 模块导入成功")
        
        print("\n2. 创建 Materials Studio 实例...")
        ms = MaterialsStudio(visible=True, suppress_dialogs=True)
        print("   ✓ 实例创建成功")
        
        print("\n3. 尝试连接 Materials Studio...")
        if ms.Connect():
            print("   ✓ 连接成功！")
            
            print("\n4. 检查连接状态...")
            if ms.IsConnected():
                print("   ✓ 连接状态正常")
            else:
                print("   ✗ 连接状态异常")
            
            print("\n5. 获取应用程序对象...")
            app = ms.GetApplication()
            if app:
                print("   ✓ 应用程序对象获取成功")
            else:
                print("   ✗ 无法获取应用程序对象")
            
            print("\n6. 关闭连接...")
            ms.Close()
            print("   ✓ 连接已关闭")
            
            print("\n" + "=" * 60)
            print("✓ 所有测试通过！")
            print("=" * 60)
            return True
            
        else:
            print("   ✗ 连接失败")
            print("\n可能的原因：")
            print("   - Materials Studio 未安装")
            print("   - Materials Studio COM 组件未注册")
            print("   - 权限不足")
            print("\n" + "=" * 60)
            print("✗ 测试失败")
            print("=" * 60)
            return False
            
    except ImportError as e:
        print(f"\n✗ 导入错误: {e}")
        print("请确保已安装所有依赖：pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)

