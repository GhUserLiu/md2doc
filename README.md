# Markdown 转 Word 转换工具

一个符合中文公文格式规范（GB/T 9704-2012）的 Markdown 转 Word 转换工具。

## ✨ 特性

- ✅ 完全符合中文公文格式规范（GB/T 9704-2012）
- 📝 支持批量转换多个 Markdown 文件
- 🎯 精确的格式控制（字体、行距、缩进等）
- 📄 支持 Word 和 PDF 双格式导出
- 🧹 自动清理 Markdown 格式标记（粗体、斜体、代码）
- 🚀 简单易用，双击运行
- 🧪 模块化设计，可作为 Python 库使用

## 🚀 快速开始

### Windows 用户（推荐）

**双击运行以下批处理文件：**

- `运行.bat` - 仅导出 Word 文档
- `运行PDF.bat` - 同时导出 Word 和 PDF 文档

### 命令行使用

```bash
# 激活虚拟环境
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 转换为 Word
python md2doc.py

# 转换为 Word + PDF
python md2doc.py -p

# 转换指定文件
python md2doc.py -f input/文档.md

# 运行测试
python tests/test_converter.py
```

## 📖 格式规范

| 项目 | 设置 |
|------|------|
| **正文字体** | 仿宋_GB2312，3号 (16pt) |
| **标题字体** | 一级：方正小标宋简体，2号 (22pt)<br>二级：黑体，3号 (16pt)<br>三级：楷体，3号 (16pt) |
| **正文行距** | 固定值 28pt |
| **首行缩进** | 2字符 |
| **段前/段后间距** | 0pt（不额外空行） |
| **页边距** | 上3.7cm、下3.5cm、左2.8cm、右2.6cm |
| **格式处理** | 自动移除粗体(`**`)、斜体(`*`)、代码(` `` `)标记 |
| **全局样式** | 禁用下划线、禁用彩色字体 |

详见：[docs/reference/完整格式规范.md](docs/reference/完整格式规范.md)

## 📁 项目结构

```text
md2doc/
├── src/md2doc/          # 核心代码
│   ├── config.py       # 配置管理
│   ├── converter.py    # 转换器核心（含格式化和解析）
│   └── cli.py          # 命令行工具
├── tests/               # 单元测试
├── docs/                # 文档
│   ├── guide/          # 使用指南
│   ├── reference/      # 参考文档
│   └── history/        # 历史记录
├── input/              # 输入文件
├── output/             # 输出文件
├── venv/               # 虚拟环境
├── 运行.bat            # Word 导出脚本
└── 运行PDF.bat         # Word + PDF 导出脚本
```

详细说明：[STRUCTURE.md](STRUCTURE.md)

## 💻 作为 Python 库使用

```python
from md2doc import MarkdownConverter

converter = MarkdownConverter()
doc, title = converter.convert(Path('input/document.md'))
doc.save(f'output/{title}.docx')
```

## 📚 文档

- [快速开始指南](docs/guide/快速开始.md)
- [虚拟环境使用指南](docs/guide/虚拟环境使用指南.md)
- [项目结构说明](STRUCTURE.md)
- [格式规范参考](docs/reference/完整格式规范.md)

## 🛠️ 开发

```bash
# 运行测试
python tests/test_converter.py

# 或使用便捷脚本
运行测试.bat
```

## 📦 依赖

- Python 3.8+
- python-docx >= 0.8.11
- docx2pdf >= 0.1.8 (PDF 导出功能)

## 🎯 使用示例

### Markdown 输入示例

```markdown
# 文档标题

这是正文内容。Markdown 格式标记会被自动清理：

- **加粗文本** → 加粗文本
- *斜体文本* → 斜体文本
- `代码片段` → 代码片段

## 二级标题

支持列表、表格、引用等标准 Markdown 语法。
```

### 转换效果

所有 Markdown 格式标记（`**`、`*`、`` ` ``）都会被移除，生成纯文本 Word 文档，符合中文公文规范。

## 📄 许可证

MIT License
