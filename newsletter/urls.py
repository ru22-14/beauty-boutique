from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscribe/', views.subscribe, name='subscribe'),
]


