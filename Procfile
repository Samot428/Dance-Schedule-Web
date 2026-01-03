# Procfile for Heroku, Railway, or other platforms
web: python DANCE_CALENDAR_WEB/manage.py migrate && gunicorn --chdir DANCE_CALENDAR_WEB DANCE_CALENDAR_WEB.wsgi:application --bind 0.0.0.0:$PORT
