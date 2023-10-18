from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Subscriber, Newsletter
from .forms import SubscriptionForm, NewsletterForm


from django.core.mail import EmailMessage


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


@login_required
def newsletter(request):

    if not request.user.is_superuser:
        messages.error(request, 'Admin Access Only to Newsletter')
        return redirect(reverse('home'))
        
    email_host = settings.DEFAULT_FROM_EMAIL
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receiver = form.cleaned_data.get('receiver').split(',')
            email_message = form.cleaned_data.get('message')
            mail = EmailMessage(subject, email_message, f"Beauty Boutique <{email_host}>", bcc=receiver)
            mail.content_subtype = 'html'
            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")
        else:
            messages.error(request, f'email sending failed')
        return redirect('/')
           
    form = NewsletterForm()
    form.fields['receiver'].initial = ','.join([active.email for active in Subscriber.objects.all()])
    context={
        "form": form
        }
    return render(request, 'newsletter/newsletter.html', context)