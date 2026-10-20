@echo off
setlocal
cd /d "%~dp0..\.."
title Running Pet Care Agent
echo Starting Pet Care Agent...
python "lifestyle\pet_care_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
