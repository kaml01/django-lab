#!/bin/bash
set -e

echo "Starting Django server..."

cd /home/ec2-user/django-app || exit 1
source venv/bin/activate

nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
