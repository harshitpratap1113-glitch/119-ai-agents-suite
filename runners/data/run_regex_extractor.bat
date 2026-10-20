@echo off
setlocal
cd /d "%~dp0..\.."
title Running Regex Extractor Agent
echo Starting Regex Extractor Agent...
python "data\regex_extractor_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
