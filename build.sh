#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Build Tailwind CSS assets
npm install
npm run build

python manage.py collectstatic --no-input
# Apply database migrations (creates auth_user and other tables)
python manage.py migrate --no-input

# python manage.py createsuperuser --noinput || true