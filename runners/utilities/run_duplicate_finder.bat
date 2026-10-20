@echo off
setlocal
cd /d "%~dp0..\.."
title Running Duplicate Finder Agent
echo Starting Duplicate Finder Agent...
python "utilities\duplicate_finder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
