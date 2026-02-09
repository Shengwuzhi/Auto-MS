# 项目结构说明

## 目录结构

```
AutoMS/
├── automs/                      # 核心模块包
│   ├── __init__.py             # 包初始化文件，导出主要类
│   ├── ms_application.py       # Materials Studio 应用程序接口
│   ├── ms_project.py           # 项目管理接口
│   ├── ms_structure.py         # 结构操作接口
│   ├── ms_calculation.py       # 计算任务接口
│   └── ms_utils.py             # 工具函数
│
├── examples/                    # 示例代码
│   ├── basic_usage.py          # 基本使用示例
│   ├── batch_optimization.py   # 批量优化示例
│   └── structure_analysis.py   # 结构分析示例
│
├── docs/                        # 文档
│   ├── guide.md                # 使用指南
│   └── api_reference.md        # API 参考文档
│
├── README.md                    # 项目说明文档
├── requirements.txt            # Python 依赖包
├── setup.py                    # 安装脚本
├── test_connection.py          # 连接测试脚本
├── .gitignore                  # Git 忽略文件
└── PROJECT_STRUCTURE.md        # 本文件
```

## 模块说明

### automs 核心模块

#### ms_application.py
- **MaterialsStudio 类**: 提供与 Materials Studio 应用程序的连接和管理
  - 连接/断开连接
  - 项目打开/创建/保存/关闭
  - 计算任务等待
  - 上下文管理器支持

#### ms_project.py
- **MSProject 类**: 提供项目管理功能
  - 文档列表获取
  - 文档创建/删除
  - 结构获取
  - 项目信息获取

#### ms_structure.py
- **MSStructure 类**: 提供结构操作功能
  - 分子创建
  - 结构导入/导出
  - 原子/化学键获取
  - 晶胞参数获取
  - 几何优化

#### ms_calculation.py
- **MSCalculation 类**: 提供计算任务功能
  - 几何优化
  - 单点能计算
  - 频率计算
  - 结果提取（能量、受力、频率等）
  - 收敛检查

#### ms_utils.py
- 工具函数集合
  - 安装路径查找
  - 文件格式支持
  - 数据格式化
  - 结构验证
  - 信息提取

## 示例代码

### basic_usage.py
包含 6 个基本使用示例：
1. 连接到 Materials Studio
2. 使用上下文管理器
3. 创建分子结构
4. 导入结构文件
5. 几何优化
6. 批量处理

### batch_optimization.py
演示如何批量处理多个结构文件：
- 批量导入结构
- 批量运行几何优化
- 结果汇总和导出

### structure_analysis.py
演示如何分析分子结构：
- 基本信息提取
- 原子和化学键信息
- 晶胞参数（晶体）
- 能量和受力分析
- 频率分析

## 文档

### guide.md
详细的使用指南，包括：
- 快速开始
- 基本概念
- 各模块使用方法
- 高级用法
- 常见问题

### api_reference.md
完整的 API 参考文档，包括：
- 所有类的说明
- 所有方法的参数和返回值
- 工具函数说明

## 设计理念

本项目参考了 [Aspen Plus 自动化接口](https://wenxiaoshuo.github.io/AspenWithPython/) 的设计思路：

1. **分层设计**: 将功能分为应用层、项目层、结构层和计算层
2. **Pythonic 接口**: 提供符合 Python 习惯的 API
3. **上下文管理**: 支持 `with` 语句自动管理资源
4. **错误处理**: 完善的异常处理和错误提示
5. **文档完善**: 提供详细的使用指南和 API 参考

## 使用流程

1. **安装依赖**: `pip install -r requirements.txt`
2. **测试连接**: `python test_connection.py`
3. **查看示例**: 运行 `examples/` 目录下的示例代码
4. **阅读文档**: 参考 `docs/` 目录下的文档
5. **开发应用**: 基于提供的接口开发自己的应用

## 注意事项

1. **Windows 平台**: Materials Studio 仅支持 Windows 系统
2. **COM 接口**: 需要 Materials Studio 正确安装并注册 COM 组件
3. **权限要求**: 可能需要管理员权限运行
4. **版本兼容**: 不同版本的 Materials Studio COM 接口可能略有差异
5. **具体实现**: 部分功能需要根据实际 Materials Studio 版本调整 COM 接口调用

## 扩展开发

如需扩展功能，可以：

1. **添加新的计算方法**: 在 `ms_calculation.py` 中添加新方法
2. **添加新的结构操作**: 在 `ms_structure.py` 中添加新方法
3. **添加新的工具函数**: 在 `ms_utils.py` 中添加新函数
4. **创建新的示例**: 在 `examples/` 目录下添加新示例

## 参考资源

- [Materials Studio 官方文档](https://www.3ds.com/products-services/biovia/products/molecular-modeling-simulation/biovia-materials-studio/)
- [Aspen Plus 自动化接口参考](https://wenxiaoshuo.github.io/AspenWithPython/)
- [Python COM 接口文档](https://docs.python.org/3/library/win32com.html)

