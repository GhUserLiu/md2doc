#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
命令行工具 - 批量转换Markdown到Word
"""

import sys
import io
import argparse
import logging
from pathlib import Path
from datetime import datetime

# 添加src目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from md2doc import MarkdownConverter, ConverterConfig
from docx2pdf import convert


def setup_logging(log_file=None, verbose=False):
    """配置日志系统"""
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    level = logging.DEBUG if verbose else logging.INFO
    handlers = [logging.StreamHandler(sys.stdout)]

    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding='utf-8'))

    logging.basicConfig(
        level=level,
        format=log_format,
        datefmt=date_format,
        handlers=handlers
    )
    return logging.getLogger(__name__)


def convert_single_file(md_file: Path, output_dir: Path, converter, logger, export_pdf=False) -> bool:
    """转换单个文件

    Args:
        md_file: Markdown文件路径
        output_dir: 输出目录
        converter: 转换器实例
        logger: 日志记录器
        export_pdf: 是否同时导出PDF
    """
    try:
        doc, title = converter.convert(md_file)
        if doc is None:
            return False

        # 生成输出文件名
        output_filename = f"{title}.docx"
        output_path = output_dir / output_filename

        # 保存Word文档
        doc.save(output_path)
        logger.info(f"✓ Word: {output_filename}")

        # 如果需要导出PDF
        if export_pdf:
            try:
                pdf_path = output_dir / f"{title}.pdf"
                convert(str(output_path), str(pdf_path))
                logger.info(f"✓ PDF:  {title}.pdf")
            except Exception as pdf_error:
                logger.warning(f"  PDF转换失败: {pdf_error}")

        return True

    except Exception as e:
        logger.error(f"✗ 失败: {md_file.name} - {e}")
        return False


def main():
    """主函数"""
    # 修复Windows控制台编码问题
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

    parser = argparse.ArgumentParser(
        description='Markdown 转 Word 批量转换工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 转换input文件夹中的所有md文件到output文件夹
  python -m md2doc.cli

  # 指定输入输出目录
  python -m md2doc.cli -i ./md_files -o ./word_files

  # 转换单个文件
  python -m md2doc.cli -f document.md

  # 同时导出PDF
  python -m md2doc.cli -p

  # 显示详细信息
  python -m md2doc.cli -v
        """
    )

    parser.add_argument('-i', '--input', type=str, default='input',
                       help='输入文件夹路径 (默认: input)')
    parser.add_argument('-o', '--output', type=str, default='output',
                       help='输出文件夹路径 (默认: output)')
    parser.add_argument('-f', '--file', type=str,
                       help='转换单个文件')
    parser.add_argument('-l', '--log', type=str,
                       help='日志文件路径')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='显示详细日志')
    parser.add_argument('-p', '--pdf', action='store_true',
                       help='同时导出PDF文件')

    args = parser.parse_args()

    # 设置日志
    logger = setup_logging(args.log, args.verbose)

    # 打印标题
    print('=' * 60)
    print('Markdown 转 Word 批量转换工具')
    print('=' * 60)
    print()

    # 创建转换器
    converter = MarkdownConverter()
    start_time = datetime.now()

    try:
        # 转换单个文件
        if args.file:
            md_file = Path(args.file)
            if not md_file.exists():
                logger.error(f"文件不存在: {args.file}")
                sys.exit(1)

            output_dir = Path(args.output)
            output_dir.mkdir(parents=True, exist_ok=True)

            logger.info(f"输出目录: {output_dir.absolute()}")
            success = convert_single_file(md_file, output_dir, converter, logger, args.pdf)

            if success:
                print()
                print('转换完成！')
            else:
                sys.exit(1)

        # 批量转换
        else:
            input_dir = Path(args.input)
            output_dir = Path(args.output)

            # 如果input目录不存在，自动创建并提示
            if not input_dir.exists():
                print('=' * 60)
                print('提示: input 文件夹不存在')
                print('=' * 60)
                print()
                print(f'已自动创建 input 文件夹: {input_dir.absolute()}')
                print()
                print('请将需要转换的 Markdown 文件 (.md) 放入该文件夹，然后重新运行程序')
                print()
                input_dir.mkdir(parents=True, exist_ok=True)

                # 创建示例文件
                sample_file = input_dir / '示例.md'
                if not sample_file.exists():
                    sample_content = """# 示例文档

这是一个示例Markdown文档。

## 一级标题

这是正文内容。支持以下特性：

- **粗体文本** - 会被自动移除格式标记
- *斜体文本* - 会被自动移除格式标记
- `代码片段` - 会被自动移除格式标记

## 二级标题

支持列表、表格等标准Markdown语法。

### 三级标题

完整的格式规范请参考项目文档。
"""
                    sample_file.write_text(sample_content, encoding='utf-8')
                    print(f'已创建示例文件: {sample_file.name}')
                print()

                sys.exit(0)

            # 创建输出目录
            output_dir.mkdir(parents=True, exist_ok=True)

            logger.info(f"输入目录: {input_dir.absolute()}")
            logger.info(f"输出目录: {output_dir.absolute()}")

            # 查找所有md文件
            md_files = list(input_dir.glob('*.md')) + list(input_dir.glob('*.markdown'))

            if not md_files:
                logger.warning('未找到任何 Markdown 文件')
                sys.exit(0)

            logger.info(f"找到 {len(md_files)} 个文件")

            # 转换文件
            results = {
                'success': 0,
                'failed': 0,
                'skipped': 0
            }

            for md_file in md_files:
                if convert_single_file(md_file, output_dir, converter, logger, args.pdf):
                    results['success'] += 1
                else:
                    results['failed'] += 1

            # 打印结果
            elapsed_time = (datetime.now() - start_time).total_seconds()
            print()
            print('=' * 60)
            print('转换完成！')
            print(f'  成功: {results["success"]}')
            print(f'  跳过: {results["skipped"]}')
            print(f'  失败: {results["failed"]}')
            print(f'  耗时: {elapsed_time:.2f} 秒')
            print(f'  输出: {output_dir.absolute()}')
            print('=' * 60)

    except KeyboardInterrupt:
        logger.info('\n用户中断操作')
        sys.exit(1)
    except Exception as e:
        logger.error(f'发生错误: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
