@echo off
setlocal
cd /d "%~dp0..\.."
title Running Data Anomaly Detector Agent
echo Starting Data Anomaly Detector Agent...
python "data\data_anomaly_detector_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
