import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery('dcelery')
app.config_from_object('django.conf:settings', namespace='CELERY') # look for any settings starting wih CELERY in settings.py

app.conf.task_routes = {'newapp.tasks.task1': {'queue': 'queue1'}, 'newapp.tasks.task2': {'queue': 'queue2'}}
app.autodiscover_tasks() # this tells celery to look in other files to find tasks i.e. tasks.py