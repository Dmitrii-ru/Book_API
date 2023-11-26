from django.dispatch import receiver
from .models import CustomUser
from django.db.models.signals import post_save
from .tasks import send_wellcome_mail_task
from .serializers import CustomUserSerializer


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance: CustomUser, created, **kwargs):
    if created:
        send_wellcome_mail_task.delay(CustomUserSerializer(instance).data)