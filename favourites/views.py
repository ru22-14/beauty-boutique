from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from products.models import Product


def view_favourites(request):
    """ View that renders favourites page content """

    return render(request, 'favourites/favourites.html')


def add_to_favourites(request, product_id):
    """ View to add/remove products to/from favourites """

    product = get_object_or_404(Product, pk=product_id)
    if product.user_favourites.filter(id=request.user.id).exists():
        product.user_favourites.remove(request.user)
        messages.info(request, 'Removed from Favourites!')
    else:
        product.user_favourites.add(request.user)
        messages.info(request, 'Successfully added to Favourites!')
    return HttpResponseRedirect(request.META["HTTP_REFERER"],)
