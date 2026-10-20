@echo off
setlocal
cd /d "%~dp0..\.."
title Running Synonym Finder Agent
echo Starting Synonym Finder Agent...
python "education\synonym_finder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
