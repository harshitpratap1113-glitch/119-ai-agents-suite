@echo off
setlocal
cd /d "%~dp0..\.."
title Running Newsletter Agent
echo Starting Newsletter Agent...
python "writing\newsletter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
