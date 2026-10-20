@echo off
setlocal
cd /d "%~dp0..\.."
title Running Timestamp Converter Agent
echo Starting Timestamp Converter Agent...
python "utilities\timestamp_converter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
