@echo off
setlocal
cd /d "%~dp0..\.."
title Running Sentiment Analyzer Agent
echo Starting Sentiment Analyzer Agent...
python "data\sentiment_analyzer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
