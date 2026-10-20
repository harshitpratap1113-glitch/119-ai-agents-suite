@echo off
setlocal
cd /d "%~dp0..\.."
title Running Ip Lookup Agent
echo Starting Ip Lookup Agent...
python "utilities\ip_lookup_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
