@echo off
setlocal
cd /d "%~dp0..\.."
title Running Math Tutor Agent
echo Starting Math Tutor Agent...
python "education\math_tutor_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
