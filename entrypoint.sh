#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $PG_HOST $PG_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
exec "$@"
