from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages



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
        #                       f'quantity to {basket[item_id]}'))
    else:
        basket[item_id] = quantity
        # messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url) 

def update_basket(request, item_id):
    """ Adjust the products in the basket """  

    quantity = int(request.POST.get('quantity')) 
    basket = request.session.get('basket', {})          

    if quantity > 0:

        basket[item_id] = quantity
                    # messages.success(request,
                    #                     (f'Updated {product.name} '
                    #                      f'quantity to {basket[item_id]}'))
    else:
        basket.pop(item_id)
                    # messages.success(request,
                    #                      (f'Removed {product.name} '
                    #                       f'from your basket'))


    request.session['basket'] = basket
    return redirect(reverse('view_basket'))     

