# GUI 使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动应用

```bash
python run_gui.py
```

浏览器会自动打开，访问 `http://localhost:8501`

## 使用场景

### 场景 1: 快速优化单个分子

**目标**: 优化水分子结构

**步骤**:
1. 选择 "🤖 AI 对话模式"
2. 输入: "优化水分子结构，使用 Forcite 计算"
3. 点击 "🔍 解析指令"
4. 确认方案后点击 "🚀 确认并执行"

### 场景 2: 批量计算

**目标**: 批量优化多个分子

**步骤**:
1. 选择 "🧱 步骤构建模式"
2. 添加步骤: "批量处理"
3. 输入分子式列表（每行一个）:
   ```
   H2O
   NH3
   CH4
   ```
4. 选择计算方法: Forcite
5. 点击 "🚀 开始自动化运行"

### 场景 3: 参数扫描

**目标**: 扫描 cutoff energy 参数

**步骤**:
1. 选择 "🧱 步骤构建模式"
2. 添加步骤: "创建分子" (例如: Si)
3. 添加步骤: "参数扫描"
4. 设置参数:
   - 参数名称: cutoff_energy
   - 参数值: 300,400,500,600
   - 计算方法: CASTEP
5. 点击 "🚀 开始自动化运行"

## 自然语言示例

### 示例 1: 几何优化

**输入**: "优化苯分子 C6H6 的结构，使用 Forcite，力场选择 COMPASS"

**解析结果**:
```json
{
  "structure": "C6H6",
  "operation": "Geometry Optimization",
  "calculator": "Forcite",
  "parameters": {
    "forcefield": "COMPASS",
    "task": "Geometry Optimization"
  }
}
```

### 示例 2: 单点能计算

**输入**: "计算硅单胞的单点能，使用 CASTEP，精度 Fine，截断能 400 eV"

**解析结果**:
```json
{
  "structure": "Si",
  "operation": "Energy",
  "calculator": "CASTEP",
  "parameters": {
    "functional": "GGA-PBE",
    "quality": "Fine",
    "cutoff_energy": 400
  }
}
```

### 示例 3: 表面计算

**输入**: "建立一个金的 3x3x1 超胞，切 (111) 面，然后用 CASTEP 算一下单点能"

**解析结果**:
```json
{
  "structure": "Au",
  "operation": "Energy",
  "calculator": "CASTEP",
  "parameters": {
    "h": 1,
    "k": 1,
    "l": 1,
    "a": 3,
    "b": 3,
    "c": 1
  }
}
```

## 步骤构建模式示例

### 工作流 1: 结构优化流程

```
步骤 1: 创建分子
  - 分子式: H2O
  - 名称: Water

步骤 2: Forcite 计算
  - 任务类型: Geometry Optimization
  - 力场: COMPASS
  - 精度: Fine
```

### 工作流 2: 能带结构计算

```
步骤 1: 创建分子
  - 分子式: Si

步骤 2: CASTEP 计算
  - 任务类型: Band Structure
  - 泛函: GGA-PBE
  - 精度: Fine
  - 截断能: 400 eV
```

## 常见问题

### Q: 如何保存工作流？

A: 在步骤构建模式中，点击 "💾 保存流程" 按钮。

### Q: 如何加载之前保存的工作流？

A: 点击 "📂 加载流程" 按钮，选择之前保存的工作流文件。

### Q: LLM 翻译不准确怎么办？

A: 
1. 尝试更清晰的描述
2. 使用步骤构建模式（不依赖 LLM）
3. 检查 LLM API Key 是否正确

### Q: 计算执行失败怎么办？

A:
1. 检查 Materials Studio 是否正常连接
2. 检查结构是否正确创建
3. 查看错误信息，调整参数

### Q: 可以离线使用吗？

A: 可以。使用本地模拟模式（不配置 LLM API Key），但翻译准确性会降低。

## 最佳实践

1. **首次使用**: 建议先使用步骤构建模式，熟悉操作流程
2. **复杂任务**: 使用步骤构建模式，逐步添加步骤
3. **简单任务**: 使用 AI 对话模式，快速完成
4. **批量任务**: 使用批量处理功能，提高效率
5. **参数优化**: 使用参数扫描功能，找到最优参数

## 技术支持

如有问题，请参考：
- [项目 README](../README.md)
- [GUI README](gui/README.md)
- [架构文档](../ARCHITECTURE.md)

