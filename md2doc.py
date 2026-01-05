#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动脚本 - 运行转换工具
"""

import sys
from pathlib import Path

# 添加src目录到路径
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from md2doc.cli import main

if __name__ == '__main__':
    main()
