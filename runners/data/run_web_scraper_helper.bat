@echo off
setlocal
cd /d "%~dp0..\.."
title Running Web Scraper Helper Agent
echo Starting Web Scraper Helper Agent...
python "data\web_scraper_helper_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
