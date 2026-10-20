@echo off
setlocal
cd /d "%~dp0..\.."
title Running Science Tutor Agent
echo Starting Science Tutor Agent...
python "education\science_tutor_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
