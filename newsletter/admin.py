from django.contrib import admin
from .models import Subscriber

class AddSubscriber(admin.ModelAdmin):
    """Class to display Subscribers on admin site"""
    list_display = ('email')
    

admin.site.register(Subscriber)


