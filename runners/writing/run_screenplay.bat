@echo off
setlocal
cd /d "%~dp0..\.."
title Running Screenplay Agent
echo Starting Screenplay Agent...
python "writing\screenplay_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
