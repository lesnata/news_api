from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery.schedules import crontab

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_api.settings')

app = Celery('news_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'reset-every-24-hours': {
        'task': 'api.tasks.reset_upvote',
        'schedule': crontab(minute=0, hour=0),
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
