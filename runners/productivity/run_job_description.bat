@echo off
setlocal
cd /d "%~dp0..\.."
title Running Job Description Agent
echo Starting Job Description Agent...
python "productivity\job_description_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
