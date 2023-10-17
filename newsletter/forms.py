from django import forms
from.models import Subscriber

class SubscriptionForm(forms.ModelForm):
    """ Create a Subscription Form """
    class Meta:
        model = Subscriber
        fields = ('email', 'confirmed',)
    