@echo off
setlocal
cd /d "%~dp0..\.."
title Running Decision Helper Agent
echo Starting Decision Helper Agent...
python "productivity\decision_helper_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
