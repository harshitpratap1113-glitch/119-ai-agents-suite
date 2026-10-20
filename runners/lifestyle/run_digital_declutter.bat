@echo off
setlocal
cd /d "%~dp0..\.."
title Running Digital Declutter Agent
echo Starting Digital Declutter Agent...
python "lifestyle\digital_declutter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
