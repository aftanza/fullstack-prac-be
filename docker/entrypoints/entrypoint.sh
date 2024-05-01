#!/bin/bash

python manage.py makemigrations
python manage.py migrate --noinput
# python manage.py collectstatic --no-input --clear
# python manage.py test

# echo "from django.contrib.auth.models import User;" \
#      "User.objects.filter(username='${ADMIN_USER}').exists() or " \
#      "User.objects.create_superuser('${ADMIN_USER}', '${ADMIN_EMAIL}', '${ADMIN_PASSWORD}')" \
#      "| exit(1)" | python manage.py shell

python manage.py create_update_superuser

exec "$@"