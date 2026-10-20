@echo off
setlocal
cd /d "%~dp0..\.."
title Running Market Researcher Agent
echo Starting Market Researcher Agent...
python "productivity\market_researcher_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
