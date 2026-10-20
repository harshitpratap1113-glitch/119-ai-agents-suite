@echo off
setlocal
cd /d "%~dp0..\.."
title Running Project Breakdown Agent
echo Starting Project Breakdown Agent...
python "productivity\project_breakdown_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
