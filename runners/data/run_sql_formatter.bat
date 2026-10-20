@echo off
setlocal
cd /d "%~dp0..\.."
title Running Sql Formatter Agent
echo Starting Sql Formatter Agent...
python "data\sql_formatter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
