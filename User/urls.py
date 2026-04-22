from django.urls import path
from .  import views

urlpatterns = [
    path('', views.Login), # Переход на страницу Login вызываеться views.Login

]
