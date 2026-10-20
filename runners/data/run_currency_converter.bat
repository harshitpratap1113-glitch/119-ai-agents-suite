@echo off
setlocal
cd /d "%~dp0..\.."
title Running Currency Converter Agent
echo Starting Currency Converter Agent...
python "data\currency_converter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
