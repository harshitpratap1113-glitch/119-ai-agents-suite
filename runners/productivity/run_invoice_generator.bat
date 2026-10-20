@echo off
setlocal
cd /d "%~dp0..\.."
title Running Invoice Generator Agent
echo Starting Invoice Generator Agent...
python "productivity\invoice_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
