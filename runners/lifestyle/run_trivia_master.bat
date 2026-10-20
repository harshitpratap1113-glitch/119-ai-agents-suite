@echo off
setlocal
cd /d "%~dp0..\.."
title Running Trivia Master Agent
echo Starting Trivia Master Agent...
python "lifestyle\trivia_master_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
