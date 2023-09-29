from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_favourites(request):
    """View that renders favourites page content"""

    return render(request, 'favourites/favourites.html',)

def add_to_favourites(request, product_id):
    """View to add/remove products to/from favourites"""

    product = get_object_or_404(Product, pk=product_id)
    if product.user_favourites.filter(id=request.user.id).exists():
        product.user_favourites.remove(request.user)
        messages.success(request, 'Product removed from Favourites!')
    else:
         product.user_favourites.add(request.user)
         messages.success(request, 'Successfully added to Favourites!')   
    return render(request, 'favourites/favourites.html')

def product_favourite_list(request, id):
    user=request.user
    favourite_products = user.favourites.all()
    
    context = {
        'favourite_products': favourite_products
    }

    return render(request, 'favourites/product_favourite_list.html', context)  



