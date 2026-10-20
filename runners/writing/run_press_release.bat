@echo off
setlocal
cd /d "%~dp0..\.."
title Running Press Release Agent
echo Starting Press Release Agent...
python "writing\press_release_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
