from django.urls import path
from .  import views
from .views import home, register_view, login_view, logout_view

urlpatterns = [
    path('', views.login_view, name='Login'),
    path('Register', views.register_view, name='Register'),
    path('HomePage', views.HomePage, name='HomePage'),
    path('Menu', views.Menu_view, name='Menu'),
    path('basket/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    # Исправлено здесь:
    path('UserBasket', views.Basket_view, name='basket'), # Имя 'basket'
    path('basket/add/<int:food_id>/', views.basket_add, name='basket_add'), 
    path('bake/<int:pk>', views.food_detail, name='food_detail'),
]