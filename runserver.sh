python manage.py collectstatic --no-input

python manage.py migrate

gunicorn --worker-tmp-dir /tmp kuntcrm.wsgi