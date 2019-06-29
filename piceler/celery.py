import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piceler.settings')

app = Celery('piceler')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()