@echo off
setlocal
cd /d "%~dp0..\.."
title Running Csv Summarizer Agent
echo Starting Csv Summarizer Agent...
python "data\csv_summarizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
