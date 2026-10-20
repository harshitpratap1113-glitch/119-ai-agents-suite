@echo off
setlocal
cd /d "%~dp0..\.."
title Running Xml To Json Agent
echo Starting Xml To Json Agent...
python "data\xml_to_json_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
