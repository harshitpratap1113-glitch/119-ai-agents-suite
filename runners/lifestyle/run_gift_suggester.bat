@echo off
setlocal
cd /d "%~dp0..\.."
title Running Gift Suggester Agent
echo Starting Gift Suggester Agent...
python "lifestyle\gift_suggester_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
