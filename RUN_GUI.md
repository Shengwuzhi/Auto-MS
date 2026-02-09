# 运行 GUI 指南

## ✅ 测试状态

所有测试已通过，GUI 可以正常运行！

## 🚀 启动 GUI

### 方法 1: 使用启动脚本（推荐）

```bash
cd C:\weizh\cursor\AutoMS
python run_gui.py
```

### 方法 2: 直接使用 Streamlit

```bash
cd C:\weizh\cursor\AutoMS
streamlit run gui/app.py
```

### 方法 3: 使用 Python 模块

```bash
cd C:\weizh\cursor\AutoMS
python -m streamlit run gui/app.py
```

## 🌐 访问界面

启动后：
- 浏览器会自动打开
- 如果没有自动打开，手动访问: **http://localhost:8501**

## 📋 使用前检查

### 必需依赖 ✅
- ✓ Streamlit: 1.54.0
- ✓ Requests: 2.32.5
- ✓ NumPy: 2.3.4
- ✓ Pandas: 2.3.3
- ✓ Matplotlib: 3.10.7
- ✓ pywin32: 已安装

### 可选依赖（LLM 支持）
- ⚠ OpenAI: 未安装（可选）
- ⚠ Google Generative AI: 未安装（可选）

**注意**: 可选依赖未安装不影响基本功能，可以使用本地模拟模式。

## 🎯 功能验证

### 已测试功能 ✅
- ✅ 模块导入正常
- ✅ LLM 翻译器工作正常
- ✅ 执行器可以初始化
- ✅ 可视化器可以初始化
- ✅ 代码语法正确

### 测试结果
```
输入: "优化水分子结构，使用 Forcite 计算"
输出: {
  "structure": "H2O",
  "operation": "Geometry Optimization",
  "calculator": "Forcite",
  "parameters": {}
}
```

## 💡 使用提示

### AI 对话模式
1. 选择 "🤖 AI 对话模式"
2. 输入自然语言描述
3. 点击 "🔍 解析指令"
4. 确认并执行

### 步骤构建模式
1. 选择 "🧱 步骤构建模式"
2. 添加步骤
3. 配置参数
4. 执行工作流

## ⚠️ 注意事项

1. **Materials Studio**: 
   - GUI 可以正常启动和运行
   - 实际计算需要 Materials Studio 已安装
   - 可以在未安装 MS 的情况下测试界面

2. **LLM API**:
   - 当前使用本地模拟模式（无需 API Key）
   - 如需使用 AI 翻译，需要配置 API Key

3. **端口占用**:
   - 默认端口: 8501
   - 如果端口被占用，Streamlit 会自动使用其他端口

## 🛠️ 故障排除

### 问题 1: 无法启动
**解决**: 检查依赖是否安装
```bash
python check_dependencies.py
```

### 问题 2: 端口被占用
**解决**: 使用其他端口
```bash
streamlit run gui/app.py --server.port=8502
```

### 问题 3: 模块导入错误
**解决**: 确保在项目根目录运行
```bash
cd C:\weizh\cursor\AutoMS
python run_gui.py
```

## 📚 相关文档

- [GUI 使用指南](GUI_USAGE.md)
- [GUI 实现文档](GUI_IMPLEMENTATION.md)
- [测试结果](GUI_TEST_RESULT.md)

---

**状态**: ✅ **可以运行**  
**最后测试**: 2025-02-07

