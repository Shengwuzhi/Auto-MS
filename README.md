# Materials Studio 自动化接口

👋 欢迎使用 Materials Studio 自动化接口项目！

本项目参考 [Aspen Plus 自动化接口](https://wenxiaoshuo.github.io/AspenWithPython/) 的设计思路，为 Materials Studio 提供 Python 自动化接口封装，采用**三层架构设计**，让分子建模和模拟自动化变得更加简单。

## 📖 项目简介

Materials Studio 是 Dassault Systèmes BIOVIA 公司开发的分子建模和模拟软件。本项目通过 Python 封装 Materials Studio 的 COM 自动化接口，采用三层架构设计：

### 三层架构

1. **底层 (Driver Layer)**: COM 接口封装，负责 Python 与 Materials Studio 的通讯
2. **中层 (Wrapper Layer)**: 封装具体的计算模块（CASTEP, DMol3, Forcite 等）和结构操作
3. **上层 (Workflow Layer)**: 业务逻辑，如批量计算、参数扫描、收敛性测试

### 主要功能

- 自动化创建和操作分子结构
- 支持多种计算模块（Forcite, CASTEP, DMol3）
- 批量运行计算任务
- 参数扫描和优化
- 收敛性测试
- 自动提取和分析计算结果
- 与 Python 科学计算生态系统的无缝集成

详细架构说明请参考 [ARCHITECTURE.md](ARCHITECTURE.md)

## 🚀 快速开始

### 环境要求

- Windows 操作系统（Materials Studio 仅支持 Windows）
- Materials Studio 已安装并配置
- Python 3.7+
- pywin32 库（用于 COM 接口）

### 安装依赖

```bash
pip install -r requirements.txt
```

### 🖥️ 使用 Web GUI（推荐）

**专为不熟悉 Materials Studio 和 Python 的学生设计**

```bash
# 启动 Web 界面
python run_gui.py
```

浏览器会自动打开，提供两种使用模式：

1. **🤖 AI 对话模式**: 通过自然语言描述想法
   - 例如："优化水分子结构，使用 Forcite 计算"
   - 支持 LLM 翻译（GPT/Gemini/DeepSeek）

2. **🧱 步骤构建模式**: 通过步骤向导描述操作
   - 可视化添加步骤
   - 保存和加载工作流
   - 适合复杂任务

详细使用说明请参考 [GUI 使用指南](GUI_USAGE.md)

### 基本使用示例

```python
from automs import MaterialsStudio

# 连接到 Materials Studio
ms = MaterialsStudio()

# 打开或创建项目
ms.OpenProject("MyProject.xsd")

# 创建分子结构
molecule = ms.CreateMolecule("C6H6")  # 创建苯分子

# 运行几何优化
ms.RunGeometryOptimization(molecule)

# 获取结果
energy = ms.GetEnergy(molecule)
print(f"优化后的能量: {energy} eV")

# 关闭连接
ms.Close()
```

## 📁 项目结构

```
AutoMS/
├── automs/                  # 核心模块（三层架构）
│   ├── __init__.py
│   ├── driver/              # 底层：COM 接口封装
│   │   ├── __init__.py
│   │   ├── ms_com_driver.py      # COM 驱动
│   │   └── ms_application.py     # 应用程序接口
│   ├── wrapper/             # 中层：计算模块和结构操作
│   │   ├── __init__.py
│   │   ├── calculators.py        # 计算模块（Forcite, CASTEP, DMol3）
│   │   └── structure_ops.py       # 结构操作
│   └── workflow/            # 上层：业务逻辑
│       ├── __init__.py
│       ├── batch_calculator.py   # 批量计算
│       ├── parameter_scan.py    # 参数扫描
│       └── convergence_test.py  # 收敛性测试
├── gui/                     # Web GUI 界面
│   ├── __init__.py
│   ├── app.py               # Streamlit 主应用
│   ├── llm_translator.py    # LLM 翻译器
│   ├── executor.py          # 任务执行器
│   ├── visualizer.py        # 结构可视化器
│   └── README.md           # GUI 使用说明
├── examples/                # 示例代码
│   ├── basic_usage.py       # 基本使用示例
│   ├── batch_optimization.py # 批量优化示例
│   └── structure_analysis.py # 结构分析示例
├── docs/                    # 文档
│   ├── guide.md             # 使用指南
│   └── api_reference.md     # API 参考
├── requirements.txt         # 依赖包
├── run_gui.py              # GUI 启动脚本
└── README.md               # 本文件
```

## 📚 功能特性

### 🖥️ Web GUI 界面（新增）
- **AI 对话模式**: 自然语言驱动的自动化
  - 支持多种 LLM（GPT/Gemini/DeepSeek）
  - 自动生成计算方案
  - 一键执行
- **步骤构建模式**: 可视化工作流构建
  - 支持多种操作类型
  - 保存/加载工作流
  - 批量处理支持

### 底层 (Driver Layer)
- COM 接口封装
- 应用程序连接和管理
- 项目管理（打开、保存、关闭）

### 中层 (Wrapper Layer)
- **计算模块封装**:
  - Forcite（分子力学）
  - CASTEP（第一性原理）
  - DMol3（密度泛函理论）
- **结构操作**:
  - 创建分子结构
  - 导入/导出结构文件
  - 结构编辑和修改
  - 晶体结构操作

### 上层 (Workflow Layer)
- **批量计算**: 批量处理多个结构
- **参数扫描**: 参数优化和扫描
- **收敛性测试**: 计算收敛性分析

## 🔧 开发计划

- [x] 基础 COM 接口封装
- [x] 应用和项目管理
- [x] 基本结构操作
- [ ] 完整计算任务支持
- [ ] 高级结果分析
- [ ] 批量处理工具
- [ ] 可视化集成

## 📝 使用许可

本项目仅供学习和研究使用。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📬 联系方式

如有问题或建议，欢迎通过以下方式联系：
- 提交 GitHub Issue
- 发送邮件

---

**注意**: 本项目需要 Materials Studio 软件支持。请确保已正确安装 Materials Studio 并拥有合法授权。

