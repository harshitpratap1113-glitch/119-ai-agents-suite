@echo off
setlocal
cd /d "%~dp0"
title Master Coordinator Agent
echo Starting Master Coordinator Agent...
python master_agent.py %*
echo.
echo ==================================================
pause
