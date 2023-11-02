from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    """Model for Subscriber's list"""
    email = models.EmailField(unique=True, null=True)
    created_date = models.DateTimeField('Date created', default=timezone.now)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    """Model for sending newletters"""
    subject = models.CharField(max_length=50, null=True)
    receiver = models.CharField(max_length=100)
    message = models.TextField(null=True)

    def __str__(self):
        return f'{self.subject}'
