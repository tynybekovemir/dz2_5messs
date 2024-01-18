
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ваш_проект.settings')

app = Celery('ваш_проект')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'начисление-монет-в-начале-месяца': {
        'task': 'exchange.tasks.award_coins',
        'schedule': crontab(day_of_month='1'),  # Начало каждого месяца
    },
}

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'сгорание-монет-в-конце-месяца': {
        'task': 'exchange.tasks.burn_coins',
        'schedule': crontab(day_of_month='last'),  # Конец каждого месяца
    },
}