from django.urls import path
from .  import views
from .views import home, register_view, login_view, logout_view

urlpatterns = [
    
    path('', views.login_view, name = 'Login'),
    path('Register', views.register_view, name='Register'),
    path('HomePage',views.HomePage, name='HomePage'),
    path('Menu',views.Menu_view, name='Menu'),
    path('bake/<int:pk>', views.food_detail, name='food_detail'),
]