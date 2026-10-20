@echo off
setlocal
cd /d "%~dp0..\.."
title Running Bibliography Formatter Agent
echo Starting Bibliography Formatter Agent...
python "education\bibliography_formatter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
