@echo off
setlocal
cd /d "%~dp0..\.."
title Running Base64 Encoder Agent
echo Starting Base64 Encoder Agent...
python "utilities\base64_encoder_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
