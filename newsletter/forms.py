from django import forms
from.models import Subscriber

class SubscriptionForm(forms.Form):
    """ Create a Subscription Form """
    email = forms.EmailField(label='Your email',
                        max_length=100,
                        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    