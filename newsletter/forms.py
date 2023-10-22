from django import forms
from tinymce.widgets import TinyMCE
from .models import Subscriber, Newsletter


class SubscriptionForm(forms.ModelForm):
    """ Create a Subscription Form """
    class Meta:
        model = Subscriber
        fields = ('email', 'confirmed',)


class NewsletterForm(forms.ModelForm):
    """Create Newsletters for subscribers"""
    message = forms.CharField(widget=TinyMCE(), label="Email content")
    
    class Meta:
        model = Newsletter
        fields = ['subject', 'receiver']
       
     
