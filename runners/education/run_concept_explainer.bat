@echo off
setlocal
cd /d "%~dp0..\.."
title Running Concept Explainer Agent
echo Starting Concept Explainer Agent...
python "education\concept_explainer_agent.py" %*
echo.
echo ==================================================
echo Agent execution finished.
pause
