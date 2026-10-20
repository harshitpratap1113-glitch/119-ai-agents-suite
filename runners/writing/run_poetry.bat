@echo off
setlocal
cd /d "%~dp0..\.."
title Running Poetry Agent
echo Starting Poetry Agent...
python "writing\poetry_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
