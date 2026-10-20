@echo off
setlocal
cd /d "%~dp0..\.."
title Running Port Scanner Agent
echo Starting Port Scanner Agent...
python "utilities\port_scanner_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
