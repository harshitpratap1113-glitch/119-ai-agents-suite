@echo off
setlocal
cd /d "%~dp0..\.."
title Running Travel Itinerary Agent
echo Starting Travel Itinerary Agent...
python "utilities\travel_itinerary_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
