@echo off
setlocal
cd /d "%~dp0..\.."
title Running Adventure Game Agent
echo Starting Adventure Game Agent...
python "lifestyle\adventure_game_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
