from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='product'),
    path('create', CreateProduct.as_view(), name='create_product'),
    path('update/<int:pk>', UpdateProduct.as_view(), name='update_product'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='delete_product'),

    
    path('brands', Brands.as_view(), name='brands'),
    path('brand/create', CreateBrand.as_view(), name='create_brand'),
    path('brand/update/<int:pk>', UpdateBrand.as_view(), name='update_brand'),
    path('brand/delete/<int:pk>', DeleteBrand.as_view(), name='delete_brand'),
]