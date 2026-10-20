@echo off
setlocal
cd /d "%~dp0..\.."
title Running File Organizer Agent
echo Starting File Organizer Agent...
python "utilities\file_organizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
