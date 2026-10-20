@echo off
setlocal
cd /d "%~dp0..\.."
title Running Data Anonymizer Agent
echo Starting Data Anonymizer Agent...
python "data\data_anonymizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
