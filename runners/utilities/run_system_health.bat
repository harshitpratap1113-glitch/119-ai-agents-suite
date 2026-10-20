@echo off
setlocal
cd /d "%~dp0..\.."
title Running System Health Agent
echo Starting System Health Agent...
python "utilities\system_health_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
