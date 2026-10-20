@echo off
setlocal
cd /d "%~dp0..\.."
title Running Regex Generator Agent
echo Starting Regex Generator Agent...
python "coding\regex_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
