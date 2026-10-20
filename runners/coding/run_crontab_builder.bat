@echo off
setlocal
cd /d "%~dp0..\.."
title Running Crontab Builder Agent
echo Starting Crontab Builder Agent...
python "coding\crontab_builder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
