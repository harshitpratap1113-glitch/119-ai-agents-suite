@echo off
setlocal
cd /d "%~dp0..\.."
title Running Daily Affirmation Agent
echo Starting Daily Affirmation Agent...
python "lifestyle\daily_affirmation_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
