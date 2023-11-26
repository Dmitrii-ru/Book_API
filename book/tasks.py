from celery import shared_task
from .utils.send_mail import send_wellcome_mail


@shared_task
def send_wellcome_mail_task(obj):
    send_wellcome_mail(obj)
