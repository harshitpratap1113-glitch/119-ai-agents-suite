@echo off
setlocal
cd /d "%~dp0..\.."
title Running Flashcard Creator Agent
echo Starting Flashcard Creator Agent...
python "education\flashcard_creator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
