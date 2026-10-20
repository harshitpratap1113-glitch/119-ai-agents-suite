@echo off
setlocal
cd /d "%~dp0..\.."
title Running Bug Finder Agent
echo Starting Bug Finder Agent...
python "coding\bug_finder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
