#!/bin/sh

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Running makemigrations and migrate"
python manage.py makemigrations
python manage.py migrate

# echo "Running makemigrations and migrate explicitly to website (often fixes some first-time run issues)"
# python manage.py makemigrations website
# python manage.py migrate website

# Start server
echo "Starting server"
# python manage.py runserver
python manage.py runserver 0.0.0.0:8000
