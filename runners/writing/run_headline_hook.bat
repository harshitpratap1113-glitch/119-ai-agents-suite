@echo off
setlocal
cd /d "%~dp0..\.."
title Running Headline Hook Agent
echo Starting Headline Hook Agent...
python "writing\headline_hook_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
