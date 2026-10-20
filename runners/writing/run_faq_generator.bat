@echo off
setlocal
cd /d "%~dp0..\.."
title Running Faq Generator Agent
echo Starting Faq Generator Agent...
python "writing\faq_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
