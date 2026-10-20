@echo off
setlocal
cd /d "%~dp0..\.."
title Running Seo Optimizer Agent
echo Starting Seo Optimizer Agent...
python "writing\seo_optimizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
