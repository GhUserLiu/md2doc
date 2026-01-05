@echo off
REM md2doc 项目测试脚本 - 自动激活虚拟环境并运行测试
echo ============================================
echo   运行 md2doc 单元测试
echo ============================================
echo.

REM 检查虚拟环境是否存在
if not exist "venv\Scripts\activate.bat" (
    echo [错误] 虚拟环境不存在！
    echo.
    echo 请先运行以下命令创建虚拟环境:
    echo   python -m venv venv
    echo   venv\Scripts\activate
    echo   pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 运行测试
python tests\test_converter.py

echo.
pause
