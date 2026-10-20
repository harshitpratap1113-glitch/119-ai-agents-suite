@echo off
setlocal
cd /d "%~dp0..\.."
title Running Dockerfile Generator Agent
echo Starting Dockerfile Generator Agent...
python "coding\dockerfile_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
