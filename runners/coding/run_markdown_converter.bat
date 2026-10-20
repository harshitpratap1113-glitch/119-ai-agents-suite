@echo off
setlocal
cd /d "%~dp0..\.."
title Running Markdown Converter Agent
echo Starting Markdown Converter Agent...
python "coding\markdown_converter_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
