@echo off
setlocal
cd /d "%~dp0..\.."
title Running Interior Design Agent
echo Starting Interior Design Agent...
python "lifestyle\interior_design_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
