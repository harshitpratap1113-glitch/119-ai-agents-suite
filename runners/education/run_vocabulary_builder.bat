@echo off
setlocal
cd /d "%~dp0..\.."
title Running Vocabulary Builder Agent
echo Starting Vocabulary Builder Agent...
python "education\vocabulary_builder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
