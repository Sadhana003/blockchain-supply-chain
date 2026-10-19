@echo off
title BlockTrack DApp Launcher
color 0B
echo ========================================================
echo       BlockTrack Supply Chain Blockchain DApp
echo ========================================================
echo.
echo Starting local web server...
echo.

where py >nul 2>nul
if %errorlevel% equ 0 (
    py "%~dp0serve.py"
    goto end
)

where python >nul 2>nul
if %errorlevel% equ 0 (
    python "%~dp0serve.py"
    goto end
)

if exist "C:\Users\komal\AppData\Local\Python\bin\python.exe" (
    "C:\Users\komal\AppData\Local\Python\bin\python.exe" "%~dp0serve.py"
    goto end
)

echo Python was not found in PATH.
echo Opening index.html directly in your default browser...
start "" "%~dp0index.html"

:end
pause
