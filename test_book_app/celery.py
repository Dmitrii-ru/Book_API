from celery import Celery
import os

broker_connection_retry_on_startup = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_book_app.settings')
app = Celery('test_book_app', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

