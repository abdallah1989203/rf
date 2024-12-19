@echo off
echo Creating virtual environment...
python -m venv .venv
call .venv\Scripts\activate.bat
echo Installing requirements...
cd backend
pip install -r requirements.txt
echo Virtual environment is ready!
echo To activate the virtual environment later, run: .venv\Scripts\activate.bat
pause
