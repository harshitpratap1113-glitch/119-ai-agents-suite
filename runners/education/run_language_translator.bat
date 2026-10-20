@echo off
setlocal
cd /d "%~dp0..\.."
title Running Language Translator Agent
echo Starting Language Translator Agent...
python "education\language_translator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
