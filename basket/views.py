from django.shortcuts import render

# Create your views here.
def view_basket(request):
    """View that renders basket page content"""

    return render(request, 'basket/basket.html')

