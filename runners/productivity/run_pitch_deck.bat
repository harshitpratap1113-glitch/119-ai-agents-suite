@echo off
setlocal
cd /d "%~dp0..\.."
title Running Pitch Deck Agent
echo Starting Pitch Deck Agent...
python "productivity\pitch_deck_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
