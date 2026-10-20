@echo off
setlocal
cd /d "%~dp0..\.."
title Running Seo Meta Optimizer Agent
echo Starting Seo Meta Optimizer Agent...
python "writing\seo_meta_optimizer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
