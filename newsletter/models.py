from django.db import models

class Subscriber(models.Model):
    """Model for Subscriber's list"""
    email = models.EmailField(unique=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"

