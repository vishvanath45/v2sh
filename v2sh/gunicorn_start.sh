#!/bin/bash

NAME="v2sh"
DIR=/home/v2sh/
DJANGO_SETTINGS_MODULE=v2sh.settings
DJANGO_WSGI_MODULE=v2sh.wsgi
LOG_LEVEL=debug
LOG_FILE=/home/vnds_20150389/v2sh/v2sh/logs/gunicorn.log

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

exec gunicorn ${DJANGO_WSGI_MODULE}:application -b 127.0.0.1:80 \
--name $NAME \
--log-level=$LOG_LEVEL \
--log-file=$LOG_FILE
