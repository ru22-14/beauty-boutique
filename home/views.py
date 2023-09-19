from django.shortcuts import render


def index(request):
    """View to return to home page"""

    return render(request, 'home/index.html')
