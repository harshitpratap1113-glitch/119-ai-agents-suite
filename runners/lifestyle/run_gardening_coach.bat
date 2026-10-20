@echo off
setlocal
cd /d "%~dp0..\.."
title Running Gardening Coach Agent
echo Starting Gardening Coach Agent...
python "lifestyle\gardening_coach_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
