$ErrorActionPreference = "Stop"

Write-Host "Creating virtual environment (if missing)..."
if (!(Test-Path "venv")) {
    python -m venv venv
} else {
    Write-Host "venv already exists!"
}

Write-Host ""
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1
Write-Host ""

Write-Host "⬆ Upgrading pip..."
python -m pip install --upgrade pip
Write-Host ""

Write-Host "Installing dependencies..."
pip install -r requirements.txt
Write-Host ""

Write-Host "Running migrations..."
python manage.py migrate
Write-Host ""

Write-Host "Seeding database..."
python manage.py seed
Write-Host ""

Write-Host "Starting server..."
python manage.py runserver