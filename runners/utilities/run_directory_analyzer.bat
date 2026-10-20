@echo off
setlocal
cd /d "%~dp0..\.."
title Running Directory Analyzer Agent
echo Starting Directory Analyzer Agent...
python "utilities\directory_analyzer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
