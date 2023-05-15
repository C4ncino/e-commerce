from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from products.models import Product
from .models import Cart, Order
from datetime import datetime as dt
from users.permissions import CLIENT_PERMS

# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.all()

        try:
            user_group = request.user.groups.all()[0].name
        except:
            user_group = ''

        context = {'products': products, 'user_group' : user_group}
        return render(request, 'shopping/products.html', context)

class CurrentCart(PermissionRequiredMixin, View):
    permission_required = CLIENT_PERMS
    login_url = "/users/login"

    def get(self, request):
        user = User.objects.get(id = request.user.id)
        currentCart = Cart.objects.get_or_create(user = user, date__isnull = True)[0]
        orders = Order.objects.filter(cart = currentCart)

        context = {'cart' : currentCart, 'orders' : orders, 'nOrders' : len(orders)}
        return render(request, 'shopping/cart.html', context)

class AddProductToCart(PermissionRequiredMixin, View):
    permission_required = CLIENT_PERMS
    login_url = "/users/login"

    def get(self, request, pk):
        user = User.objects.get(id = request.user.id)
        cart = Cart.objects.get_or_create(user = user, date__isnull = True)[0]
        product = Product.objects.get(id = pk)

        Order.objects.create(cart = cart, product=product)

        product.stock -= 1
        product.save()

        cart.cost = cart.cost + product.price
        cart.save()
        
        messages.success(request, ("Product Added To Cart!"))
        return redirect('shopping')
    
class DeleteProductFromCart(PermissionRequiredMixin, View):
    permission_required = CLIENT_PERMS
    login_url = "/users/login"
    
    def get(self, request, pk):
        user = User.objects.get(id = request.user.id)
        cart = Cart.objects.get(user = user, date__isnull = True)
        order = Order.objects.get(id = pk)
        product = order.product
        
        order.delete()

        product.stock += 1
        product.save()
 
        cart.cost = cart.cost - product.price
        cart.save()
        
        messages.success(request, ("Product Deleted From Cart!"))
        return redirect('cart')

class Purchase(PermissionRequiredMixin, View):
    permission_required = CLIENT_PERMS
    login_url = "/users/login"
    
    def get(self, request, pk):
        cart = Cart.objects.get(id = pk)
        now = dt.now()

        cart.date = now
        cart.save()
        
        messages.success(request, ("Purchase made Successfully!"))
        return redirect('record')

class Record(PermissionRequiredMixin, View):
    permission_required = CLIENT_PERMS
    login_url = "/users/login"

    def get(self, request):
        user = User.objects.get(id = request.user.id)
        carts = Cart.objects.filter(user = user, date__isnull = False)
        data = []
        for cart in carts:
            orders =   Order.objects.filter(cart = cart)
            info = {'cart' : cart, 'orders' : orders}
            data.append(info)
            
        context = {'carts' : data, 'nCarts' : len(carts)}
        return render(request, 'shopping/record.html', context)
