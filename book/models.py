from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    author = models.CharField(max_length=50, blank=False, null=False)
    publication = models.PositiveIntegerField(blank=False, null=False)
    isbn = models.CharField(
        max_length=13,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    email = models.EmailField(blank=False, null=False)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
