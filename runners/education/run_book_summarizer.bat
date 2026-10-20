@echo off
setlocal
cd /d "%~dp0..\.."
title Running Book Summarizer Agent
echo Starting Book Summarizer Agent...
python "education\book_summarizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
