@echo off
setlocal
cd /d "%~dp0..\.."
title Running Json Schema Agent
echo Starting Json Schema Agent...
python "coding\json_schema_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
