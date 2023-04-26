from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from products.forms import ProductCreate
from products.models import Product, Brand

# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
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
            return render(request, 'products/products.html', {'form': form})

class UpdateProduct(View):  
    def get(self, request, pk):
        
        product = Product.objects.get(id=pk)
        form = ProductCreate(instance = product)

        context = {'form': form}
        return render(request, 'products/form.html', context)
          
    def post(self, request, pk):

        product = get_object_or_404(Product, id=pk)

        form = ProductCreate(initial={'name': product.name})

        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            print("FORM ERROR!")
            print(form.errors)
            return render(request, 'products/products.html', {'form': form})
        

class Brands(View):
    def get(self, request):
        brands = Brand.objects.all()
        context = {'brands' : brands}
        return render(request, 'products/brands.html', context)


# class CreateBrand(View):
#     def get(self, request):
