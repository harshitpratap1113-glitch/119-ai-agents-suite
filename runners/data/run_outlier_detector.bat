@echo off
setlocal
cd /d "%~dp0..\.."
title Running Outlier Detector Agent
echo Starting Outlier Detector Agent...
python "data\outlier_detector_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
