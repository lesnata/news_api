from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import News


@shared_task
def reset_upvote():
    news = News.objects.all()
    for i in news:
        print(f'i is {i}')
        i.upvote = 0
        i.save()
        return 'Upvote counter is set to 0'
