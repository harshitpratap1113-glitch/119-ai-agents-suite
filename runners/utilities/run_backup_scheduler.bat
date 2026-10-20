@echo off
setlocal
cd /d "%~dp0..\.."
title Running Backup Scheduler Agent
echo Starting Backup Scheduler Agent...
python "utilities\backup_scheduler_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
