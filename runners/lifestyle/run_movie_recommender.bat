@echo off
setlocal
cd /d "%~dp0..\.."
title Running Movie Recommender Agent
echo Starting Movie Recommender Agent...
python "lifestyle\movie_recommender_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
