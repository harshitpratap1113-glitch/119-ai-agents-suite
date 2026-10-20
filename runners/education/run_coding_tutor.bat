@echo off
setlocal
cd /d "%~dp0..\.."
title Running Coding Tutor Agent
echo Starting Coding Tutor Agent...
python "education\coding_tutor_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
