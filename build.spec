# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller配置文件 - md2doc打包
使用方法: pyinstaller build.spec
"""

block_cipher = None

a = Analysis(
    ['md2doc.py'],  # 主程序入口
    pathex=[],
    binaries=[],
    datas=[
        # 包含配置文件（如果需要）
        # ('src/md2doc/*.py', 'md2doc'),
    ],
    hiddenimports=[
        # 明确指定隐藏导入
        'docx',
        'docx.oxml',
        'docx.oxml.ns',
        'docx.shared',
        'docx.enum',
        'docx2pdf',
        'win32com',
        'win32com.client',
        'lxml',
        'lxml._elementpath',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 排除不需要的模块以减小体积
        'tkinter',
        'matplotlib',
        'pandas',
        'numpy',
        'scipy',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='md2doc',  # 可执行文件名称
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # 使用UPX压缩（如果可用）
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # 可以添加自定义图标路径
)
