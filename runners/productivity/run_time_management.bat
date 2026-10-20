@echo off
setlocal
cd /d "%~dp0..\.."
title Running Time Management Agent
echo Starting Time Management Agent...
python "productivity\time_management_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
