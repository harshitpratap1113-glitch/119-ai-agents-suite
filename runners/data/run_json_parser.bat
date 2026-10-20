@echo off
setlocal
cd /d "%~dp0..\.."
title Running Json Parser Agent
echo Starting Json Parser Agent...
python "data\json_parser_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
