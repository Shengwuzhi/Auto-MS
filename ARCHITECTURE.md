# 系统架构设计

## 三层架构

Materials Studio 与 Aspen Plus 不同，Aspen 是流程模拟，MS 是微观结构模拟。MS 2023 依然保留了强大的 COM (Component Object Model) 接口，同时也极度依赖内部的 MaterialsScript (Perl)。

为了"更优化更完整"，采用三层架构：

### 底层 (Driver Layer): COM 接口封装

**职责**: 负责 Python 与 Materials Studio 的通讯（COM 接口封装）

**模块**:
- `automs/driver/ms_com_driver.py`: COM 驱动，最底层的 COM 接口通信
- `automs/driver/ms_application.py`: 应用程序接口，基于 COM 驱动提供应用程序级别的操作

**特点**:
- 不包含业务逻辑
- 只负责 COM 连接和基本操作
- 提供最底层的接口

**示例**:
```python
from automs.driver import MSComDriver, MSApplication

# 使用 COM 驱动
driver = MSComDriver()
driver.connect()

# 使用应用程序接口
app = MSApplication(driver)
app.new_project("MyProject")
```

### 中层 (Wrapper Layer): 计算模块和结构操作封装

**职责**: 封装具体的计算模块（CASTEP, DMol3, Forcite 等）和结构操作

**模块**:
- `automs/wrapper/calculators.py`: 计算模块封装
  - `CalculatorBase`: 计算器基类
  - `ForciteCalculator`: Forcite 计算器（分子力学）
  - `CASTEPCalculator`: CASTEP 计算器（第一性原理）
  - `DMol3Calculator`: DMol3 计算器（密度泛函理论）
- `automs/wrapper/structure_ops.py`: 结构操作封装
  - `StructureOperations`: 结构创建、导入、导出、编辑

**特点**:
- 封装具体的计算模块
- 提供统一的接口
- 处理结构相关的操作

**示例**:
```python
from automs.driver import MSApplication
from automs.wrapper import ForciteCalculator, StructureOperations

app = MSApplication()
app.connect()

# 结构操作
structure_ops = StructureOperations(app)
molecule = structure_ops.create_molecule("H2O")

# 计算
calculator = ForciteCalculator(app)
calculator.set_input_document(molecule)
calculator.set_parameters(forcefield="COMPASS", task="Geometry Optimization")
calculator.run()
```

### 上层 (Workflow Layer): 业务逻辑

**职责**: 业务逻辑，如批量计算、参数扫描、收敛性测试

**模块**:
- `automs/workflow/batch_calculator.py`: 批量计算
  - `BatchCalculator`: 批量处理多个结构
- `automs/workflow/parameter_scan.py`: 参数扫描
  - `ParameterScanner`: 参数扫描和优化
- `automs/workflow/convergence_test.py`: 收敛性测试
  - `ConvergenceTester`: 计算收敛性测试

**特点**:
- 实现业务逻辑
- 提供高级功能
- 组合使用中层模块

**示例**:
```python
from automs.driver import MSApplication
from automs.wrapper import ForciteCalculator, StructureOperations
from automs.workflow import BatchCalculator

app = MSApplication()
app.connect()

# 批量计算
batch_calc = BatchCalculator(app)
structures = [structure_ops.create_molecule("H2O"), ...]
calculator = ForciteCalculator(app)
results = batch_calc.batch_optimize(structures, calculator)
```

## 架构优势

1. **分层清晰**: 每层职责明确，易于维护和扩展
2. **易于扩展**: 可以轻松添加新的计算模块或工作流
3. **代码复用**: 底层和中层可以被多个工作流复用
4. **测试友好**: 每层可以独立测试

## 目录结构

```
automs/
├── driver/              # 底层：COM 接口封装
│   ├── __init__.py
│   ├── ms_com_driver.py
│   └── ms_application.py
│
├── wrapper/             # 中层：计算模块和结构操作
│   ├── __init__.py
│   ├── calculators.py
│   └── structure_ops.py
│
└── workflow/            # 上层：业务逻辑
    ├── __init__.py
    ├── batch_calculator.py
    ├── parameter_scan.py
    └── convergence_test.py
```

## 使用流程

### 基本使用（三层架构）

```python
# 1. 底层：连接
from automs.driver import MSApplication
app = MSApplication()
app.connect()

# 2. 中层：结构操作和计算
from automs.wrapper import ForciteCalculator, StructureOperations

structure_ops = StructureOperations(app)
molecule = structure_ops.create_molecule("H2O")

calculator = ForciteCalculator(app)
calculator.set_input_document(molecule)
calculator.set_parameters(forcefield="COMPASS")
calculator.run()

# 3. 上层：批量处理
from automs.workflow import BatchCalculator
batch_calc = BatchCalculator(app)
results = batch_calc.batch_optimize(structures, calculator)
```

### 向后兼容（旧接口）

为了保持向后兼容，仍然可以使用旧的接口：

```python
from automs import MaterialsStudio, MSStructure, MSCalculation

# 这些实际上是新架构的别名
ms = MaterialsStudio()  # 等同于 MSApplication
structure = MSStructure(ms)  # 等同于 StructureOperations
calculation = MSCalculation(ms)  # 等同于 CalculatorBase
```

## 扩展指南

### 添加新的计算模块

1. 在 `automs/wrapper/calculators.py` 中继承 `CalculatorBase`
2. 实现 `create_task()`, `set_input_document()`, `set_parameters()` 方法
3. 在 `__init__.py` 中导出

### 添加新的工作流

1. 在 `automs/workflow/` 中创建新文件
2. 使用中层模块实现业务逻辑
3. 在 `__init__.py` 中导出

## 设计原则

1. **单一职责**: 每层只负责一个方面
2. **依赖倒置**: 上层依赖中层，中层依赖底层
3. **开闭原则**: 对扩展开放，对修改关闭
4. **接口隔离**: 提供清晰的接口，隐藏实现细节

