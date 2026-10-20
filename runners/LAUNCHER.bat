@echo off
setlocal
cd /d "%~dp0..\.."
title Running Launcher Agent
echo Starting Launcher Agent...
python "runners\LAUNCHER_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
