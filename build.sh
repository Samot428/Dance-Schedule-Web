#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
cd DANCE_CALENDAR_WEB
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Build complete!"
