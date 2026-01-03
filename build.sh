#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting Python path..."
export PYTHONPATH="${PWD}:${PYTHONPATH}"

echo "Collecting static files..."
python DANCE_CALENDAR_WEB/manage.py collectstatic --no-input

echo "Running database migrations..."
python DANCE_CALENDAR_WEB/manage.py migrate

echo "Build complete!"
