@echo off
setlocal
cd /d "%~dp0..\.."
title Running Flashcard Generator Agent
echo Starting Flashcard Generator Agent...
python "education\flashcard_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
