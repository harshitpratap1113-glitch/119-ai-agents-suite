@echo off
setlocal
cd /d "%~dp0..\.."
title Running Syllabus Gap Finder Agent
echo Starting Syllabus Gap Finder Agent...
python "education\syllabus_gap_finder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
