from django.contrib import admin
from .models import Subscriber, Newsletter

class AddSubscriber(admin.ModelAdmin):
    """Class to display Subscribers on admin site"""
    list_display = ('email', 'created_date')


class AdminNewsletters(admin.ModelAdmin):
    """Class to display Subscribers on admin site"""
    list_display = ('subject', 'receiver', 'message')

admin.site.register(Subscriber)
admin.site.register(Newsletter)


