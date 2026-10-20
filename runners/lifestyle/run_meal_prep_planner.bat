@echo off
setlocal
cd /d "%~dp0..\.."
title Running Meal Prep Planner Agent
echo Starting Meal Prep Planner Agent...
python "lifestyle\meal_prep_planner_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
