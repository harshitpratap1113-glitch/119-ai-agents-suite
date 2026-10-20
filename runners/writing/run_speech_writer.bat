@echo off
setlocal
cd /d "%~dp0..\.."
title Running Speech Writer Agent
echo Starting Speech Writer Agent...
python "writing\speech_writer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
