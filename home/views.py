from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        context = {'products':['carteras', 'teléfonos', 'carteras', 'mochilas', 'tennis']}
        return render(request, 'index.html', context)