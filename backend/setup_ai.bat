@echo off
setlocal

echo --- Khedut Bandhu Professional AI Setup ---

:: 1. Create a Virtual Environment specifically using Python 3.12
echo Step 1: Creating Private AI Environment (Python 3.12)...

:: Try py -3.12
py -3.12 -m venv myenv 2>nul
if %errorlevel% equ 0 goto success

:: Try python
python -m venv myenv 2>nul
if %errorlevel% equ 0 goto success

echo.
echo ❌ Error: Python could not be found or virtual environment creation failed.
echo.
echo 💡 Please download and install Python 3.12 from:
echo    https://www.python.org/downloads/release/python-3120/
echo    Make sure to check "Add Python to PATH" during installation.
echo.
pause
exit /b

:success
:: 2. Activate the environment and install libraries
echo Step 2: Installing AI Libraries...
call myenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r "../ai-service/requirements.txt"

:: 3. Reorganize and Train
echo Step 3: Organizing Data and Training model...
python reorganize_data.py
python train_model.py

:: 4. Launch
echo Step 4: Starting AI Service...
start /B python "../ai-service/main.py"

echo.
echo ✅ AI Setup Complete! Your Diagnostic feature is ready.
echo.
pause
