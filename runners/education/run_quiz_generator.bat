@echo off
setlocal
cd /d "%~dp0..\.."
title Running Quiz Generator Agent
echo Starting Quiz Generator Agent...
python "education\quiz_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
