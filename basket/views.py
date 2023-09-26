from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404


# Create your views here.
def view_basket(request):
    """View that renders basket page content"""

    return render(request, 'basket/basket.html',)

def add_to_basket(request, item_id):
    """ Add quantity of the desired product to the basket """  

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') 
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        # messages.success(request,
        #                      (f'Updated {product.name} '
        #                       f'quantity to {bag[item_id]}'))
    else:
        basket[item_id] = quantity
        # messages.success(request, f'Added {product.name} to your bag')

    request.session['basket'] = basket
    return redirect(redirect_url) 

