from django.urls import path

from shop.views import *

urlpatterns = [
    path('', menu_list, name='home'),
    path('menu/<slug:menu_slug>/', punkt_menu, name='menu_list'),
]
