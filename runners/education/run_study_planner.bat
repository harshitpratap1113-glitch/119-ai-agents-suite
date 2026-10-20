@echo off
setlocal
cd /d "%~dp0..\.."
title Running Study Planner Agent
echo Starting Study Planner Agent...
python "education\study_planner_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
