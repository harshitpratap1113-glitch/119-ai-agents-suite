@echo off
setlocal
cd /d "%~dp0..\.."
title Running Url Shortener Agent
echo Starting Url Shortener Agent...
python "utilities\url_shortener_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
