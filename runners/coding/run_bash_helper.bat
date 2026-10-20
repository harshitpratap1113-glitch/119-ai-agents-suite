@echo off
setlocal
cd /d "%~dp0..\.."
title Running Bash Helper Agent
echo Starting Bash Helper Agent...
python "coding\bash_helper_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
