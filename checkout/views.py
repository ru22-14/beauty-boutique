from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is Empty')
        return redirect(reverse ('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key' : 'pk_test_51NyEiYAsQ5JfzwVK98O2Np6lisSOw0oFDd89RbafwygcAnp78uIY3paB7hBm7rPLDHBrbd9qWndlvfIpCYxyZxwI00heAlNrYf',
        'client_secret' : 'test client secret',
    }
    return render(request, template, context)

