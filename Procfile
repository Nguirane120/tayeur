web: gunicorn fewnu_compta.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py makemigrations
manage.py migrate
