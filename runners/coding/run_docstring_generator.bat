@echo off
setlocal
cd /d "%~dp0..\.."
title Running Docstring Generator Agent
echo Starting Docstring Generator Agent...
python "coding\docstring_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
