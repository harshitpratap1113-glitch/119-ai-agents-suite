@echo off
setlocal
cd /d "%~dp0..\.."
title Running Recipe Generator Agent
echo Starting Recipe Generator Agent...
python "lifestyle\recipe_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
