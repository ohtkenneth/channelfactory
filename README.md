## Usage
Login to postgres shell

`sudo su - postgres`

Log into postgres session

`psql`

Create database

`CREATE DATABASE api_geocode;`

Create user for django to connect with

`CREATE USER channelfactory WITH PASSWORD 'channelfactory';`

Allow channelfactory user to create test db

`ALTER USER channelfactory CREATEDB;`

Replace Google Api Key in /channelfactory/api/utils Line 7

    import requests
    import json

    from math import cos, asin, sqrt
    from .models import Geocode

    GOOGLE_API_KEY = YOUR_API_KEY
    GoogleApiBaseUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

Make migration

`python manage.py makemigrations api`

Migrate

`python manage.py migrate`

Run server

`python manage.py runserver`

Open browser to localhost:8000/api/geocode

## Run tests
`python manage.py test api`

## Dependencies
PostgreSQL, psycopg2
