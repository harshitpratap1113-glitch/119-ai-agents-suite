@echo off
setlocal
cd /d "%~dp0..\.."
title Running Markdown Table Agent
echo Starting Markdown Table Agent...
python "utilities\markdown_table_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
