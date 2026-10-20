@echo off
setlocal
cd /d "%~dp0..\.."
title Running Blog Post Agent
echo Starting Blog Post Agent...
python "writing\blog_post_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
