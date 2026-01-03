# Procfile for Heroku, Railway, or other platforms
web: cd DANCE_CALENDAR_WEB && python manage.py migrate && gunicorn DANCE_CALENDAR_WEB.wsgi:application --bind 0.0.0.0:$PORT
