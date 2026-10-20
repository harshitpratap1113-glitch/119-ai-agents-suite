@echo off
setlocal
cd /d "%~dp0..\.."
title Running Copywriter Agent
echo Starting Copywriter Agent...
python "writing\copywriter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
