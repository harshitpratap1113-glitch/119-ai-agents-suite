@echo off
setlocal
cd /d "%~dp0..\.."
title Running Pdf Analyzer Agent
echo Starting Pdf Analyzer Agent...
python "data\pdf_analyzer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
