from django.contrib import admin
from django.urls import include

from shop.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
