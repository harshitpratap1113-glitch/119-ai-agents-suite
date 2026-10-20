@echo off
setlocal
cd /d "%~dp0..\.."
title Running Env Setup Guard Agent
echo Starting Env Setup Guard Agent...
python "coding\env_setup_guard_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
