import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tips_navigator.settings')

app = Celery('tips_navigator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    "runs-every-60-seconds": {
        "task": "tips.tasks.fetch_data",
        "schedule": timedelta(seconds=60),
        "args": ()
    },
}