from products.models import Product

def favourites_contents(request):
    """
    Allows access to favourites data throughout site

    """
    products = 0

    if request.user:
        products = Product.objects.filter(user_favourites=request.user)

        context = {
            "user_favourites": products,
                }    
    return(context)    
   
