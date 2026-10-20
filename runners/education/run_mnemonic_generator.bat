@echo off
setlocal
cd /d "%~dp0..\.."
title Running Mnemonic Generator Agent
echo Starting Mnemonic Generator Agent...
python "education\mnemonic_generator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
