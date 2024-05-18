#!/bin/bash

python manage.py makemigrations
python manage.py migrate --noinput
# python manage.py collectstatic --no-input --clear
# python manage.py test

python manage.py create_update_superuser

exec "$@"