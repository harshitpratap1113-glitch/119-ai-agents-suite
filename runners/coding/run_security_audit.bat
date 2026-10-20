@echo off
setlocal
cd /d "%~dp0..\.."
title Running Security Audit Agent
echo Starting Security Audit Agent...
python "coding\security_audit_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
