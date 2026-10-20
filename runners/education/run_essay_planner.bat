@echo off
setlocal
cd /d "%~dp0..\.."
title Running Essay Planner Agent
echo Starting Essay Planner Agent...
python "education\essay_planner_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
