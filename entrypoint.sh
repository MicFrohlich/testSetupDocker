#!/usr/bin/env bash
# Create's any new migrations
python manage.py makemigrations
# Runs any un-run migrations
python manage.py migrate
# In a docker container we need to run the server to look on all local ip's
# Thats why we use 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000