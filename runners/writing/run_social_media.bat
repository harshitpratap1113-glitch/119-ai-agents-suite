@echo off
setlocal
cd /d "%~dp0..\.."
title Running Social Media Agent
echo Starting Social Media Agent...
python "writing\social_media_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
