@echo off
setlocal
cd /d "%~dp0..\.."
title Running Workout Planner Agent
echo Starting Workout Planner Agent...
python "lifestyle\workout_planner_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
