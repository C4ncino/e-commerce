from django.shortcuts import render
from django.views import View

# Create your views here.
class Products (View):
    def get(self, request):
        products = [] #TODO: Hacer la querry
        context = {'products': products}
        return render(request, 'products.html', context)