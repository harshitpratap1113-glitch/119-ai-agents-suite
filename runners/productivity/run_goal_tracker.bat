@echo off
setlocal
cd /d "%~dp0..\.."
title Running Goal Tracker Agent
echo Starting Goal Tracker Agent...
python "productivity\goal_tracker_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
