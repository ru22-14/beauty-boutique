from django.shortcuts import render, redirect, reverse
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
        form = SubscriptionForm(request.POST)
        email = request.POST.get('email', None)
        if form.is_valid():
            subscribed_user = Subscriber.objects.filter(email=email).first() 
            if subscribed_user:
                messages.error(request, 'This Account has already been registered!')
                return redirect(request.META.get("HTTP_REFERER", "/"))

            else:
                form.save()
                messages.success(request, 'You are registered Successfully!')
                return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = SubscriptionForm()
    context = {
        'form' : form,
    }  
    return render(request, 'home/index.html', context)                 



