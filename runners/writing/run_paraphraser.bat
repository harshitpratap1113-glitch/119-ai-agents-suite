@echo off
setlocal
cd /d "%~dp0..\.."
title Running Paraphraser Agent
echo Starting Paraphraser Agent...
python "writing\paraphraser_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
