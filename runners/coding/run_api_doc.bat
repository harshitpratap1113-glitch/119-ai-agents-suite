@echo off
setlocal
cd /d "%~dp0..\.."
title Running Api Doc Agent
echo Starting Api Doc Agent...
python "coding\api_doc_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
