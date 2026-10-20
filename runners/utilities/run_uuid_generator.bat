@echo off
setlocal
cd /d "%~dp0..\.."
title Running Uuid Generator Agent
echo Starting Uuid Generator Agent...
python "utilities\uuid_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
