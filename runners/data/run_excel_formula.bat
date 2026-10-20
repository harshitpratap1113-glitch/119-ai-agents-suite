@echo off
setlocal
cd /d "%~dp0..\.."
title Running Excel Formula Agent
echo Starting Excel Formula Agent...
python "data\excel_formula_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
