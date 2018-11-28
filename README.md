## Usage
1. Login to postgres shell

`sudo su - postgres`

2. Start psql session

`psql`

3. Create database

`CREATE DATABASE api_geocode;`

4. Create user for django to connect with

`CREATE USER channelfactory WITH PASSWORD 'channelfactory';`

5. Allow channelfactory user to create test db

`ALTER USER channelfactory CREATEDB;`

6. Replace Google Api Key in /channelfactory/api/utils Line 7

    import requests
    import json

    from math import cos, asin, sqrt
    from .models import Geocode

    GOOGLE_API_KEY = YOUR_API_KEY
    GoogleApiBaseUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

7. Make migration

`python manage.py makemigrations api`

8. Migrate

`python manage.py migrate`

9. Run server

`python manage.py runserver`

10. Open browser to localhost:8000/api/geocode

## Run tests
`python manage.py test api`

## Dependencies
PostgreSQL, psycopg2
