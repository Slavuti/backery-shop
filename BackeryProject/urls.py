from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls') ),  # Переадресация на маршрутизатор User.urls 
    path('orders/', include('orders.urls') )  # Переадресация на маршрутизатор orders.urls 
]
