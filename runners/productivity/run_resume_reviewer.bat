@echo off
setlocal
cd /d "%~dp0..\.."
title Running Resume Reviewer Agent
echo Starting Resume Reviewer Agent...
python "productivity\resume_reviewer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
