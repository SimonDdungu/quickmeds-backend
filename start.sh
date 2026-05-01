#!/usr/bin/env bash
set -e

echo "Creating virtual environment (if missing)..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
else
    echo "venv already exists!"
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

echo "Upgrading pip..."
python3 -m pip install --upgrade pip
echo ""

echo "Installing dependencies..."
pip install -r requirements.txt
echo ""

echo "Running migrations..."
python3 manage.py migrate
echo ""

echo "Seeding the database..."
python3 manage.py seed
echo ""

echo "Starting server..."
python3 manage.py runserver