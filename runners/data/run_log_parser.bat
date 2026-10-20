@echo off
setlocal
cd /d "%~dp0..\.."
title Running Log Parser Agent
echo Starting Log Parser Agent...
python "data\log_parser_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
