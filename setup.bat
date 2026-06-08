@echo off
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Installing requirements...
set AIOHTTP_NO_EXTENSIONS=1
pip install -r files-mentioned-by-the-user-index\requirements.txt
echo Setup complete!
pause
