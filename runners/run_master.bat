@echo off
setlocal
cd /d "%~dp0..\.."
title Running Master Agent
echo Starting Master Agent...
python "runners\master_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
