@echo off
setlocal
cd /d "%~dp0..\.."
title Running Travel Planner Agent
echo Starting Travel Planner Agent...
python "productivity\travel_planner_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
