from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from products.models import Product
from .models import Cart

# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'shopping/products.html', context)

class CurrentCart(LoginRequiredMixin, View):
    login_url = "/users/login"

    def get(self, request, userPK):
        user = User.objects.get(id = int(userPK))
        cart = Cart.objects.get_or_create(user = user, date = None)
        context = {'cart' : cart}
        return render(request, 'shopping/cart.html', context)

class AddProductToCart(View):
    def get(self, request, userPK, productPk):
        product = Product.objects.get(id = productPk)
