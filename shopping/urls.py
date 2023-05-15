from django.urls import path
from .views import *

urlpatterns = [
    path('', Products.as_view(), name="shopping"),
    path('cart', CurrentCart.as_view(), name="cart"),
    path('add_to_cart/<int:pk>', AddProductToCart.as_view(), name="add_product"),
    path('delete_from_cart/<int:pk>', DeleteProductFromCart.as_view(), name="delete_product"),
    path('purchase/<int:pk>', Purchase.as_view(), name="purchase"),

    path('record', Record.as_view(), name="record"),
]