@echo off
setlocal
cd /d "%~dp0..\.."
title Running Project Issue Creator Agent
echo Starting Project Issue Creator Agent...
python "productivity\project_issue_creator_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
