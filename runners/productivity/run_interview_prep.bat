@echo off
setlocal
cd /d "%~dp0..\.."
title Running Interview Prep Agent
echo Starting Interview Prep Agent...
python "productivity\interview_prep_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
