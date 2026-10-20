@echo off
setlocal
cd /d "%~dp0..\.."
title Running Habit Tracker Agent
echo Starting Habit Tracker Agent...
python "lifestyle\habit_tracker_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
