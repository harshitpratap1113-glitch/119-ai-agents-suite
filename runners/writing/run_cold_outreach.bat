@echo off
setlocal
cd /d "%~dp0..\.."
title Running Cold Outreach Agent
echo Starting Cold Outreach Agent...
python "writing\cold_outreach_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
