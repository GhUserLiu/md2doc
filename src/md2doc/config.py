# -*- coding: utf-8 -*-
"""
配置模块 - 定义所有格式规范和常量
"""

from dataclasses import dataclass
from typing import Dict, Any
from docx.shared import Pt


@dataclass
class FontConfig:
    """字体配置"""
    name: str
    size: Pt
    bold: bool = False
    italic: bool = False

    def __post_init__(self):
        if isinstance(self.size, (int, float)):
            self.size = Pt(self.size)


@dataclass
class MarginConfig:
    """页边距配置（单位：cm）"""
    top: float = 3.7      # 37mm - 上边距
    bottom: float = 3.7   # 37mm - 下边距（与上边距一致）
    left: float = 2.8     # 28mm - 左边距
    right: float = 2.8    # 28mm - 右边距（与左边距一致）
    header: float = 1.5
    footer: float = 2.5


@dataclass
class ParagraphConfig:
    """段落配置"""
    line_spacing: Pt = Pt(30.5)  # 固定值30.5磅行距（符合每面22行标准）
    first_line_indent_chars: int = 2  # 首行缩进2字符
    space_before_title: Pt = Pt(0)  # 标题段前间距（不额外空行）
    space_after_title: Pt = Pt(0)  # 标题段后间距


class ConverterConfig:
    """转换器配置类"""

    # 字体规范（根据GB/T 9704-2012和CSS标准）
    FONTS = {
        'title': FontConfig('方正小标宋简体', 22, True),  # 文档主标题：2号小标宋加粗
        'heading1': FontConfig('黑体', 16, False),  # 一级标题（##）：3号黑体常规（黑体本身已醒目）
        'heading2': FontConfig('楷体', 16, False),  # 二级标题（###）：3号楷体常规（楷体本身已醒目）
        'heading3': FontConfig('仿宋_GB2312', 16, False),  # 三级标题（####）：3号仿宋常规
        'body': FontConfig('仿宋_GB2312', 16),  # 正文：3号仿宋_GB2312
        'quote': FontConfig('仿宋_GB2312', 16, italic=True),  # 引用：3号仿宋斜体
    }

    # 页边距配置
    MARGINS = MarginConfig()

    # 段落配置
    PARAGRAPH = ParagraphConfig()

    # 列表符号
    LIST_BULLET = '•'

    # 文件编码
    ENCODING = 'utf-8'

    @classmethod
    def get_font(cls, font_type: str) -> FontConfig:
        """获取字体配置"""
        return cls.FONTS.get(font_type, cls.FONTS['body'])

    @classmethod
    def as_dict(cls) -> Dict[str, Any]:
        """导出为字典"""
        return {
            'fonts': {k: {'name': v.name, 'size': v.size.pt, 'bold': v.bold, 'italic': v.italic}
                     for k, v in cls.FONTS.items()},
            'margins': {
                'top_cm': cls.MARGINS.top,
                'bottom_cm': cls.MARGINS.bottom,
                'left_cm': cls.MARGINS.left,
                'right_cm': cls.MARGINS.right,
                'header_cm': cls.MARGINS.header,
                'footer_cm': cls.MARGINS.footer,
            },
            'paragraph': {
                'line_spacing_pt': cls.PARAGRAPH.line_spacing.pt,
                'first_line_indent_chars': cls.PARAGRAPH.first_line_indent_chars,
                'space_before_title_pt': cls.PARAGRAPH.space_before_title.pt,
                'space_after_title_pt': cls.PARAGRAPH.space_after_title.pt,
            }
        }
