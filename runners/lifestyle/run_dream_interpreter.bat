@echo off
setlocal
cd /d "%~dp0..\.."
title Running Dream Interpreter Agent
echo Starting Dream Interpreter Agent...
python "lifestyle\dream_interpreter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
