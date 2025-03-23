from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_tracker.settings')

app = Celery('product_tracker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.imports = ("products.task",)

# from celery.schedules import crontab

# app.conf.beat_schedule = {
#     'fetch-coinbase-data-every-hour': {
#         'task': 'products.tasks.fetch_coinbase_data',
#         'schedule': crontab(minute=0, hour='*'),  # Every hour
#     },
# }

# app.conf.beat_schedule = {
#     'fetch_coinbase_data_every_hour': {
#         'task': 'products.tasks.fetch_coinbase_data',
#         'schedule': 3600.0,  # Every hour
#     },
# }
