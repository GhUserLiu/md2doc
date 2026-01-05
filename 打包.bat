@echo off
REM md2doc 项目打包脚本
echo ============================================
echo   md2doc 可执行文件打包工具
echo ============================================
echo.

REM 检查虚拟环境是否存在
if not exist "venv\Scripts\activate.bat" (
    echo [错误] 虚拟环境不存在！
    echo.
    echo 请先运行以下命令创建虚拟环境:
    echo   python -m venv venv
    echo   venv\Scripts\activate
    echo   pip install -r requirements-build.txt
    echo.
    pause
    exit /b 1
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 检查PyInstaller是否已安装
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [信息] PyInstaller未安装，正在安装...
    pip install pyinstaller>=6.0.0
    echo.
)

REM 清理旧的打包文件
echo [1/3] 清理旧的打包文件...
if exist "build" rmdir /s /q build
if exist "dist\md2doc.exe" del /f /q dist\md2doc.exe
echo 完成！
echo.

REM 开始打包
echo [2/3] 开始打包...
echo 使用PyInstaller创建单文件可执行程序...
echo.

pyinstaller build.spec

if errorlevel 1 (
    echo.
    echo [错误] 打包失败！
    pause
    exit /b 1
)

echo.
echo [3/3] 打包完成！
echo.
echo ============================================
echo   可执行文件位置
echo ============================================
echo.
echo 文件路径: dist\md2doc.exe
echo.
echo 使用方法:
echo   md2doc.exe                # 转换所有Markdown文件
echo   md2doc.exe -p             # 转换并导出PDF
echo   md2doc.exe -f 文件.md     # 转换指定文件
echo.
echo ============================================

REM 询问是否测试运行
echo.
set /p test="是否立即测试运行? (y/n): "
if /i "%test%"=="y" (
    echo.
    echo [测试] 运行 md2doc.exe --help
    dist\md2doc.exe --help
    echo.
)

pause
