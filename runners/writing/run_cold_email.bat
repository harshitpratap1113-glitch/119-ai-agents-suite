@echo off
setlocal
cd /d "%~dp0..\.."
title Running Cold Email Agent
echo Starting Cold Email Agent...
python "writing\cold_email_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
