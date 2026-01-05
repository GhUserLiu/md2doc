@echo off
REM md2doc 项目运行脚本 - 自动激活虚拟环境并运行
echo ============================================
echo   Markdown 转 Word 批量转换工具
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

REM 运行转换工具
python md2doc.py %*

echo.
pause
