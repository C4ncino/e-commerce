from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='product'),
    path('create', CreateProduct.as_view(), name='create_product'),
    path('update/<int:pk>', UpdateProduct.as_view(), name='update_product'),

    
    path('brands', Brands.as_view(), name='brands'),
]