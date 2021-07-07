#!/bin/sh

echo "==========================================>"
echo "Stopping all Celery processes..."
echo "==========================================>"
kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n'  ' ') > /dev/null 2>&1

echo "Starting Celery Worker and Celery Beat in daemon mode..."
echo "==========================================>"
celery -A tips_navigator beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --logfile=celery.beat.log --detach

celery -A tips_navigator worker -l info --logfile=celery.log --detach

echo "Celery Worker and Celery Beat started!"

