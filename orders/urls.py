from django.urls import path
from .  import views

urlpatterns = [
    path('HomePage', views.HomepPage), # Переход на страницу HomePage вызываеться views.HomepPage
    path('AboutUs', views.AboutUs), # Переход на  страницу AboutUs вызываеться views.AboutUs
    path('Basket', views.Basket), # Переход на страницу Корзина/Basket вызываеться views.views.Basket
   # ПОКА НЕ ИСПОЛЬЗУЕТЬСЯ path('HomePage/<int:pk>', views.LayoutProduct), # Переход на  страницу x продукта вызываеться  views.LayoutProduct
]
