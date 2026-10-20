@echo off
setlocal
cd /d "%~dp0..\.."
title Running Proofreader Agent
echo Starting Proofreader Agent...
python "writing\proofreader_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
