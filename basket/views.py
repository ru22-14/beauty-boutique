from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_basket(request):
    """
    View that renders basket page content
    """
    
    return render(request, 'basket/basket.html',)


def add_to_basket(request, item_id):
    """ 
    Add quantity of the desired product to the basket 
    """  
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') 
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                        (f'Updated {product.name} '
                         f'quantity to {basket[item_id]}'))                         
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url) 


def update_basket(request, item_id):
    """ Adjust the products in the basket """  
    
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity')) 
    basket = request.session.get('basket', {})          

    if quantity <= 15 and quantity > 0:

        basket[item_id] = quantity
        messages.success(request,
                           (f'Updated {product.name} '
                            f'quantity to {basket[item_id]}'))
    elif quantity > 15:
        messages.warning(request, 'sorry this qunatity isnt allowed')                                      
    else:
        basket.pop(item_id)
        messages.success(request,
        (f'Removed {product.name} from your basket'))
    request.session['basket'] = basket
    return redirect(reverse('view_basket')) 


def remove_basket(request, item_id):
    """ Remove the products from the basket """ 
    try:
        product = Product.objects.get(pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id) 
        messages.success(request,
                        (f'Removed {product.name} from your basket'))       
            
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request,
            f'error removing item (e)')
        return HttpResponse(status=500)        

