from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.view_favourites), name='view_favourites'),
    path('add/<product_id>', login_required(views.add_to_favourites), name='add_to_favourites'),
]
