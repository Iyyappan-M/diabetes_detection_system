#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

chmod +x build.sh
chmod +x "diabetes_detection_system.wsgi:application"

python manage.py collectstatic --no-input
python manage.py migrate
