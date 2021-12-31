
from __future__ import absolute_import,unicode_literals

import celery

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","FastEmailCeleryServiceProject.settings")

app=celery.Celery("FastEmailCeleryServiceProject")

app.config_from_object("django.conf:settings",namespace="CELERY")

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')