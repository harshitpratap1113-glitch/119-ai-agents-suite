@echo off
setlocal
cd /d "%~dp0..\.."
title Running Hash Generator Agent
echo Starting Hash Generator Agent...
python "utilities\hash_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
