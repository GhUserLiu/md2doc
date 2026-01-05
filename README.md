# Markdown 转 Word 转换工具

一个符合中文公文格式规范（GB/T 9704-2012）的 Markdown 转 Word 转换工具。

## ✨ 特性

- ✅ 完全符合公文格式规范
- 📝 支持批量转换
- 🎯 精确的格式控制
- 🚀 简单易用，一键运行
- 🧪 模块化设计

## 🚀 快速开始

### Windows 用户（推荐）

**双击运行 `运行.bat` 即可！**

### 命令行使用

```bash
# 激活虚拟环境
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 转换文件
python md2doc.py

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
| **页边距** | 上3.7cm、下3.5cm、左2.8cm、右2.6cm |

详见：[docs/reference/完整格式规范.md](docs/reference/完整格式规范.md)

## 📁 项目结构

```
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
└── 运行.bat            # 便捷脚本
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

## 📄 许可证

MIT License
