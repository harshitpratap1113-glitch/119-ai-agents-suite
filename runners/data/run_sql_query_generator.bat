@echo off
setlocal
cd /d "%~dp0..\.."
title Running Sql Query Generator Agent
echo Starting Sql Query Generator Agent...
python "data\sql_query_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
