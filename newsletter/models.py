from django.db import models

class Subscriber(models.Model):
    """Model for Subscriber's list"""
    email = models.EmailField(unique=True, null=True)
    confirmation_number = models.CharField(max_length=20)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email}'

