import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'challenge_dev_digital_sys.settings')

app = Celery('challenge_dev_digital_sys')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
