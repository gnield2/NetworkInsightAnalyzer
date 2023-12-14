@echo off

REM Check if Python3 is installed
where python >nul 2>&1

if errorlevel 1 (
    echo Python 3 is not installed. Please install Python 3.
    exit /b 1
)

REM Check if pip3 is installed
where pip >nul 2>&1
if errorlevel 1 (
    echo pip3 is not installed. Installing pip3...
    REM You might need to set up the PATH variable to include Python's Scripts directory
    REM (e.g., set PATH=%PATH%;C:\PythonXX\Scripts)
    REM Then use 'python -m ensurepip' to install pip if it's not available
    python -m ensurepip
)

REM Install necessary Python libraries
echo Installing necessary python libraries...
pip3 uninstall speedtest
pip3 install matplotlib schedule speedtest-cli