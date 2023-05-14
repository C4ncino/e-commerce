from django.shortcuts import redirect, render
from django.views import View
from products.models import Product

# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'shopping/products.html', context)