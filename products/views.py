from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.
class Products (View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products.html', context)