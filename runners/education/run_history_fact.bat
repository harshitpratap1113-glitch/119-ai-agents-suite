@echo off
setlocal
cd /d "%~dp0..\.."
title Running History Fact Agent
echo Starting History Fact Agent...
python "education\history_fact_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
