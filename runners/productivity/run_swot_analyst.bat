@echo off
setlocal
cd /d "%~dp0..\.."
title Running Swot Analyst Agent
echo Starting Swot Analyst Agent...
python "productivity\swot_analyst_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
