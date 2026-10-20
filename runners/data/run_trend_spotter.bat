@echo off
setlocal
cd /d "%~dp0..\.."
title Running Trend Spotter Agent
echo Starting Trend Spotter Agent...
python "data\trend_spotter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
