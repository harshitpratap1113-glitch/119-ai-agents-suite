@echo off
setlocal
cd /d "%~dp0..\.."
title Running Git Commit Agent
echo Starting Git Commit Agent...
python "coding\git_commit_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
