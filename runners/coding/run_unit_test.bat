@echo off
setlocal
cd /d "%~dp0..\.."
title Running Unit Test Agent
echo Starting Unit Test Agent...
python "coding\unit_test_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
