#!/bin/bash
set -e

echo "Installing dependencies..."

cd /home/ec2-user/django-app || exit 1

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
