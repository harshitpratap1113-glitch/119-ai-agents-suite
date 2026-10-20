@echo off
setlocal
cd /d "%~dp0..\.."
title Running Calendar Time Blocker Agent
echo Starting Calendar Time Blocker Agent...
python "productivity\calendar_time_blocker_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
