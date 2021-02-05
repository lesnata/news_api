import schedule
import time
from .models import News


#TODO refactor upvote_reset with Celery:
# set up configuration, logic and docker-compose
# check out: https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html

def reset_upvote():
    news = News.objects.all()
    for i in news:
        i.upvote = 0
    return news


schedule.every().day.at("01:00").do(reset_upvote)

while True:
    schedule.run_pending()
    time.sleep(1)
