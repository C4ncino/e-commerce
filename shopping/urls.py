from django.urls import path
from .views import *

urlpatterns = [
    path('', Products.as_view(), name="shopping"),
    path('cart/<str:userPK>', CurrentCart.as_view(), name="cart"),
]