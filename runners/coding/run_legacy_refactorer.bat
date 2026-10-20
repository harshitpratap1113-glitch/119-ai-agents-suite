@echo off
setlocal
cd /d "%~dp0..\.."
title Running Legacy Refactorer Agent
echo Starting Legacy Refactorer Agent...
python "coding\legacy_refactorer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
