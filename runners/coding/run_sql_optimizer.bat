@echo off
setlocal
cd /d "%~dp0..\.."
title Running Sql Optimizer Agent
echo Starting Sql Optimizer Agent...
python "coding\sql_optimizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
