@echo off
setlocal
cd /d "%~dp0..\.."
title Running Subscription Tracker Agent
echo Starting Subscription Tracker Agent...
python "utilities\subscription_tracker_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
