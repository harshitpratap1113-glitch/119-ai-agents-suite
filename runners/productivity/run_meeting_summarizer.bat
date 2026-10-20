@echo off
setlocal
cd /d "%~dp0..\.."
title Running Meeting Summarizer Agent
echo Starting Meeting Summarizer Agent...
python "productivity\meeting_summarizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
