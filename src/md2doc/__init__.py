"""
Markdown to Word Converter
一个符合中文公文格式规范的 Markdown 转 Word 转换工具
"""

__version__ = '2.0.0'
__author__ = 'Your Name'

from .converter import MarkdownConverter
from .config import ConverterConfig

__all__ = ['MarkdownConverter', 'ConverterConfig']
