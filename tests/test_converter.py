# -*- coding: utf-8 -*-
"""
单元测试 - 转换器功能测试
"""

import unittest
from pathlib import Path
from docx import Document

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from md2doc import MarkdownConverter, ConverterConfig
from md2doc.converter import (
    parse_inline_formatting,
    extract_title_from_md,
    sanitize_filename,
    normalize_list_symbol,
    is_signature_line
)


class TestParser(unittest.TestCase):
    """测试解析器功能"""

    def test_parse_inline_formatting_bold(self):
        """测试加粗格式解析"""
        result = parse_inline_formatting("这是**加粗**文本")
        self.assertEqual(result, [('text', '这是'), ('bold', '加粗'), ('text', '文本')])

    def test_parse_inline_formatting_italic(self):
        """测试斜体格式解析"""
        result = parse_inline_formatting("这是*斜体*文本")
        self.assertEqual(result, [('text', '这是'), ('italic', '斜体'), ('text', '文本')])

    def test_parse_inline_formatting_mixed(self):
        """测试混合格式解析"""
        result = parse_inline_formatting("**加粗**和*斜体*")
        self.assertEqual(result, [('bold', '加粗'), ('text', '和'), ('italic', '斜体')])

    def test_sanitize_filename(self):
        """测试文件名清理"""
        result = sanitize_filename('测试<>:"/\\|?*文档')
        self.assertEqual(result, '测试文档')

    def test_normalize_list_symbol(self):
        """测试列表符号标准化"""
        # 测试移除列表符号
        self.assertEqual(normalize_list_symbol('- item'), 'item')
        self.assertEqual(normalize_list_symbol('* item'), 'item')
        self.assertEqual(normalize_list_symbol('+ item'), 'item')
        self.assertEqual(normalize_list_symbol('• item'), 'item')

        # 普通文本不做处理
        self.assertEqual(normalize_list_symbol('normal text'), 'normal text')


class TestFormatter(unittest.TestCase):
    """测试格式化功能"""

    def test_is_signature_line(self):
        """测试落款行识别"""
        self.assertTrue(is_signature_line('辅导员：张三'))
        self.assertTrue(is_signature_line('日期：2026年1月4日'))
        self.assertFalse(is_signature_line('这是一段普通文本'))


class TestConverterConfig(unittest.TestCase):
    """测试配置"""

    def test_font_config(self):
        """测试字体配置"""
        config = ConverterConfig()

        title_font = config.get_font('title')
        self.assertEqual(title_font.name, '方正小标宋简体')
        self.assertEqual(title_font.size.pt, 22)
        self.assertTrue(title_font.bold)

        body_font = config.get_font('body')
        self.assertEqual(body_font.name, '仿宋_GB2312')
        self.assertEqual(body_font.size.pt, 16)
        self.assertFalse(body_font.bold)


class TestIntegration(unittest.TestCase):
    """集成测试"""

    def setUp(self):
        """设置测试环境"""
        self.converter = MarkdownConverter()
        self.test_input_dir = Path(__file__).parent.parent / 'input'
        self.test_output_dir = Path(__file__).parent.parent / 'output' / 'tests'
        self.test_output_dir.mkdir(parents=True, exist_ok=True)

    def test_convert_simple_md(self):
        """测试转换简单Markdown文件"""
        # 创建测试文件
        test_md = self.test_output_dir / 'test.md'
        test_md.write_text("""# 测试标题

这是一段测试文本。

## 二级标题

这是二级标题下的内容。

### 三级标题

- 列表项1
- 列表项2

> 引用内容

落款：测试
日期：2026年1月4日
""", encoding='utf-8')

        # 转换
        doc, title = self.converter.convert(test_md)

        # 验证
        self.assertIsNotNone(doc)
        self.assertEqual(title, '测试标题')

        # 保存文档
        output_path = self.test_output_dir / '测试标题.docx'
        doc.save(output_path)
        self.assertTrue(output_path.exists())


if __name__ == '__main__':
    unittest.main()
