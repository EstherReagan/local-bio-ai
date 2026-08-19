@echo off
title Bio-AI Local Environment Initializer
echo ===================================================
echo 🧬 INITIALIZING SECURE LOCAL ENVIRONMENT CONTEXT 
echo ===================================================
echo.
echo [STEP 1] Auditing and configuring local Python modules...
pip install biopython requests
echo.
echo [STEP 2] Verifying operational connectivity to loopback engine...
curl -s http://localhost:11434/ >nul
if %errorlevel% equ 0 (
    echo Connection Status: ONLINE (Port 11434 actively listening)
) else (
    echo Connection Status: WARNING (Ensure desktop system application is active)
)
echo.
echo ===================================================
echo ✅ PIPELINE ENVIRONMENT INITIALIZED SUCCESSFULLY
echo ===================================================
pause
