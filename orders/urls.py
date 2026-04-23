from django.urls import path
from .  import views
from .views import success
from .views import cancel

from .views import create_checkout_session

urlpatterns = [
    path('pay/<int:order_id>/', create_checkout_session, name='pay'), #payments urls added 6
    path('success/', success),
    path('cancel/', cancel),
]