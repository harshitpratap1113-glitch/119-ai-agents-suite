@echo off
setlocal
cd /d "%~dp0..\.."
title Running Password Generator Agent
echo Starting Password Generator Agent...
python "utilities\password_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
