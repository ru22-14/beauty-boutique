from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings

from .models import Subscriber
from .forms import SubscriptionForm
import random


def random_digits():
    """Function to create random numbers for the purpose of confirmation"""
    return "%0.12d" % random.randint(0, 999999999999)

def subscribe(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        messages.success(request, 'Success!')

        form = SubscriptionForm()
        context = {
            'email': sub.email,
            'form': SubscriptionForm()
        }
        return render(request, context)
    else:
        return render(request, 'index.html', {'form': SubscriberForm()})