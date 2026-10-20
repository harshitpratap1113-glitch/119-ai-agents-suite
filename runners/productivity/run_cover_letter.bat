@echo off
setlocal
cd /d "%~dp0..\.."
title Running Cover Letter Agent
echo Starting Cover Letter Agent...
python "productivity\cover_letter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
