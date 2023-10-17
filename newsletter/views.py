from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriptionForm
import random


def subscribe(request):
    confirmed = False
    if request.method == 'POST':
        form = SubscriptionForm(data=request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            subscribed_user = Subscriber.objects.filter(email=email).exists()
            if not subscribed_user:
                form.save()
                confirmed = True
                messages.success(request, f'{email} is registered Successfully!')
                return redirect(request.META.get("HTTP_REFERER", "/"))
                

        else:
            messages.error(request, f'{email} has already been registered!')
            return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = SubscriptionForm()
    context = {
        'form' : form,
        'confirmed' : confirmed,
    }  
    return render(request, 'home/index.html', context)  

