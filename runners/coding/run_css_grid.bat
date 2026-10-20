@echo off
setlocal
cd /d "%~dp0..\.."
title Running Css Grid Agent
echo Starting Css Grid Agent...
python "coding\css_grid_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
