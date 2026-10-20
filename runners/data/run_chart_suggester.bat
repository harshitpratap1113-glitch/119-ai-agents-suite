@echo off
setlocal
cd /d "%~dp0..\.."
title Running Chart Suggester Agent
echo Starting Chart Suggester Agent...
python "data\chart_suggester_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
