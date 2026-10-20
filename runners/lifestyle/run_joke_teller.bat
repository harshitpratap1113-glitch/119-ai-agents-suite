@echo off
setlocal
cd /d "%~dp0..\.."
title Running Joke Teller Agent
echo Starting Joke Teller Agent...
python "lifestyle\joke_teller_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
