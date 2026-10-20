@echo off
setlocal
cd /d "%~dp0..\.."
title Running Code Refactor Agent
echo Starting Code Refactor Agent...
python "coding\code_refactor_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
