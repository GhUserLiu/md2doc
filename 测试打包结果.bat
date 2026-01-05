@echo off
REM 测试打包后的可执行文件
echo ============================================
echo   测试 md2doc 可执行文件
echo ============================================
echo.

if not exist "dist\md2doc.exe" (
    echo [错误] 找不到 dist\md2doc.exe
    echo 请先运行 "打包.bat" 生成可执行文件
    echo.
    pause
    exit /b 1
)

echo [1/3] 检查可执行文件版本信息...
dist\md2doc.exe --version
echo.

echo [2/3] 显示帮助信息...
dist\md2doc.exe --help
echo.

echo [3/3] 测试实际转换功能...
echo 正在转换 input\测试文档.md ...
echo.

dist\md2doc.exe -f "input\测试文档.md" -p

echo.
echo ============================================
echo   测试完成！
echo ============================================
echo.
echo 请检查 output\ 目录查看生成的文件
echo.
pause
