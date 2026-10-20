@echo off
setlocal
cd /d "%~dp0..\.."
title Running Expense Tracker Agent
echo Starting Expense Tracker Agent...
python "productivity\expense_tracker_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
