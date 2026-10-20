@echo off
setlocal
cd /d "%~dp0..\.."
title Running Book Recommender Agent
echo Starting Book Recommender Agent...
python "lifestyle\book_recommender_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
