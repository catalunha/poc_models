catalunha@pop-os:~/myapp/django/poc_models$ python -m venv venv


catalunha@pop-os:~/myapp/django/poc_models$ source ./venv/bin/activate
(venv) catalunha@pop-os:~/myapp/django/poc_models$ pip install django
(venv) catalunha@pop-os:~/myapp/django/poc_models$ pip install djangor
estframework
(venv) catalunha@pop-os:~/myapp/django/poc_models$ pip freeze
asgiref==3.7.2
Django==4.2.5
djangorestframework==3.14.0
pytz==2023.3.post1
sqlparse==0.4.4

(venv) catalunha@pop-os:~/myapp/django/poc_models$ django-admin startproject project .
(venv) catalunha@pop-os:~/myapp/django/poc_models$ django-admin startapp api
(venv) catalunha@pop-os:~/myapp/django/poc_models$ python manage.py migrate
(venv) catalunha@pop-os:~/myapp/django/poc_models$ python manage.py createsuperuser
Username (leave blank to use 'catalunha'): admin
Email address:  
Password: a
Password (again): a
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
