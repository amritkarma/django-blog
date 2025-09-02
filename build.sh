#!/bin/bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate

python -m pip install --no-cache-dir -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py create_superuser