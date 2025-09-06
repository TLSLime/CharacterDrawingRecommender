@echo off
echo 开始打包智能绘画角色推荐系统...

REM 清理之前的构建
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

REM 使用PyInstaller打包
pyinstaller build.spec

echo 打包完成！
echo 可执行文件位于 dist 目录中
pause
