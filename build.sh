#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='Dheeraj').exists() or User.objects.create_superuser('Dheeraj', 'admin@admin.com', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell