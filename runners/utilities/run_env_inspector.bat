@echo off
setlocal
cd /d "%~dp0..\.."
title Running Env Inspector Agent
echo Starting Env Inspector Agent...
python "utilities\env_inspector_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
