@echo off
setlocal
cd /d "%~dp0..\.."
title Running Riddle Generator Agent
echo Starting Riddle Generator Agent...
python "lifestyle\riddle_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
