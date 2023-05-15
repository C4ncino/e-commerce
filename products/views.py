from django.shortcuts import redirect, render
from django.views import View
from products.forms import ProductCreate, BrandCreate
from products.models import Product, Brand
from django.contrib.auth.mixins import PermissionRequiredMixin
from users.permissions import STAFF_PERMS

# Create your views here.
# Products CRUD
class Products(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products/products.html', context)

class CreateProduct(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request):
        form = ProductCreate()
        context = {'form': form}
        return render(request, 'products/form.html', context)
    
    def post(self, request):
        form = ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            print("FORM ERROR!")
            print(form.errors)
            return render(request, 'products/form.html', {'form': form})

class UpdateProduct(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ProductCreate(instance = product)

        context = {'form': form}
        return render(request, 'products/form.html', context)
          
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ProductCreate(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            print("FORM ERROR!")
            print(form.errors.as_data())
            return render(request, 'products/form.html', {'form': form})
  
class DeleteProduct(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        
        return redirect('product')
        
# Brands CRUD
class Brands(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request):
        brands = Brand.objects.all()
        context = {'brands' : brands}
        return render(request, 'products/brands.html', context)

class CreateBrand(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request):
        form = BrandCreate()
        context = {'form': form}
        return render(request, 'products/form_b.html', context)
    
    def post(self, request):
        form = BrandCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brands')
        else:
            print("FORM ERROR!")
            print(form.errors)
            return render(request, 'products/form_b.html', {'form': form})

class UpdateBrand(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request, pk):
        brand = Brand.objects.get(id=pk)
        form = BrandCreate(instance = brand)

        context = {'form': form}
        return render(request, 'products/form_b.html', context)
          
    def post(self, request, pk):
        brand = Brand.objects.get(id=pk)
        form = BrandCreate(request.POST, instance=brand)

        if form.is_valid():
            form.save()
            return redirect('brands')
        else:
            print("FORM ERROR!")
            print(form.errors.as_data())
            return render(request, 'products/form_b.html', {'form': form})

class DeleteBrand(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request, pk):
        brand = Brand.objects.get(id=pk)
        brand.delete()
        
        return redirect('brands')