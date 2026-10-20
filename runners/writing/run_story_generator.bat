@echo off
setlocal
cd /d "%~dp0..\.."
title Running Story Generator Agent
echo Starting Story Generator Agent...
python "writing\story_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
