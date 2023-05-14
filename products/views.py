from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from products.forms import ProductCreate, BrandCreate
from products.models import Product, Brand

# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        print(context)
        return render(request, 'products/products.html', context)
    
class CreateProduct(View):
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

class UpdateProduct(View):  
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
    

class DeleteProduct(View):  
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        
        return redirect('product')
        

class Brands(View):
    def get(self, request):
        brands = Brand.objects.all()
        context = {'brands' : brands}
        return render(request, 'products/brands.html', context)

class CreateBrand(View):
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

class UpdateBrand(View):  
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
            return redirect('product')
        else:
            print("FORM ERROR!")
            print(form.errors.as_data())
            return render(request, 'products/form_b.html', {'form': form})
    

class DeleteBrand(View):  
    def get(self, request, pk):
        brand = Brand.objects.get(id=pk)
        brand.delete()
        
        return redirect('brands')