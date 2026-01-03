#!/usr/bin/env bash
# Alternative build script - simpler approach
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python DANCE_CALENDAR_WEB/manage.py collectstatic --no-input

echo "Running database migrations..."
python DANCE_CALENDAR_WEB/manage.py migrate

echo "Build complete!"
