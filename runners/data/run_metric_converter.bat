@echo off
setlocal
cd /d "%~dp0..\.."
title Running Metric Converter Agent
echo Starting Metric Converter Agent...
python "data\metric_converter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
