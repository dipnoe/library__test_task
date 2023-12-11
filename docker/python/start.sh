#!/bin/bash

if [ "$MODE" != "CELERY" ]
then ./manage.py migrate &&
  gunicorn src.config.wsgi:application --bind 0.0.0.0:8000
fi
