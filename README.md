[![Python 3.8](https://img.shields.io/badge/python-3.8-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 4.1](https://img.shields.io/badge/Django-4.1-green.svg)
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/thomas545/ecommerce_api/blob/master/LICENSE)
<!-- ![Build](https://github.com/thomas545/ecommerce_api/workflows/Django CI/badge.svg?branch=master) -->

# Fewnu compta API
### Documentation:

1. [Django](https://docs.djangoproject.com/en/4.1/releases/4.1/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)

### Installation:

##### System Dependencies:

1. Clone or download this repo.

2. Activate the virtual environment on Linux :  
`python3 -m venv env`

3. or delete the env folder and Create your virtual environment on Linux:  
`python3 -m venv env` and activate it `source env/bin/activate`

6. Install requirements in the virtualenv:  
`pip install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):

1. Create database with name **yourdatabasename** and replace it on settings.py with you db **username** and **password**:  
##### if you run it with docker 
you should use **db** on as HOST in settings.py else **127.0.0.1**:  


2. Make Django database migrations:
`python3 manage.py makemigrations`  
then: `python3 manage.py migrate`

##### Use admin interface:

1. Create an admin user:  
`python3 manage.py createsuperuser`

2. Run the project locally:  
`python manage.py runserver`

3. Navigate to admin dashboard: `http://localhost:8000/admin/`

4. Navigate to api docs : `http://localhost:8000/api/v1/docs`



