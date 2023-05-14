from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserA

# Create your views here.
class User(View):
    def get(self, request):
        users = UserA.objects.all()
        context = {'users' : users}
        print(context)
        return render(request, 'users/users.html', context)

class Login(View):
    def get(self, request):
        return render(request, 'users/login.html', {})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error loggin, try again..."))
            return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class Register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(
            request, 
            'users/register_user.html', 
            {'form':form,}
        )
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
        