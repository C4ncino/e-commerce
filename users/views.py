from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission, User as UserA
from .forms import UserCreate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .permissions import STAFF, CLIENT, STAFF_PERMS

# Create your views here.
# CRUD USERS
class User(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request):
        users = UserA.objects.all()
        context = {'users' : users}
        return render(request, 'users/users.html', context)

class CreateUser(PermissionRequiredMixin, View):
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request):
        form = UserCreate()
        context = {'form': form}
        return render(request, 'users/form.html', context)
    
    def post(self, request):
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print("FORM ERROR!")
            print(form.errors)
            return render(request, 'users/form.html', {'form': form})

class UpdateUser(PermissionRequiredMixin, View):  
    permission_required = STAFF_PERMS
    raise_exception = True

    def get(self, request, pk):
        user = UserA.objects.get(id=pk)
        form = UserCreate(instance = user)

        context = {'form': form}
        return render(request, 'users/form.html', context)
          
    def post(self, request, pk):
        user = UserA.objects.get(id=pk)
        form = UserCreate(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print("FORM ERROR!")
            print(form.errors.as_data())
            return render(request, 'user/form.html', {'form': form})

class DeleteUser(PermissionRequiredMixin, View):  
    permission_required = STAFF_PERMS
    raise_exception = True
    
    def get(self, request, pk):
        user = UserA.objects.get(id=pk)
        user.delete()
        
        return redirect('users')

# Authentication
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

            group = Group.objects.get_or_create(name="Client")
            if group[1]:
                for p in CLIENT:
                    permission = Permission.objects.get(codename = p)
                    user.user_permissions.add(permission)
        
            user.groups.add(group[0])
            
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
        else:
            messages.success(request, ("Something Went Wrong!"))
            return redirect('register_user')

class RegisterAdmin(View):
    def get(self, request):
        form = UserCreationForm()

        return render(
            request, 
            'users/register_4dm1n.html', 
            {'form':form,}
        )
    
    def post(self, request):
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            group = Group.objects.get_or_create(name="Staff")
            if group[1]:
                for p in STAFF:
                    permission = Permission.objects.get(codename = p)
                    user.user_permissions.add(permission)
                    print(user.user_permissions.all())
        
            user.groups.add(group[0])
            
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
        else:
            messages.success(request, ("Something Went Wrong!"))
            return redirect('register_4dm1n')
        
class Update(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "users/update_user.html", {})
        else:
            return redirect('login')
        
    def post(self, request):
        newPassword = request.POST['password1']
        current_user = UserA.objects.get(id=request.user.id)
        current_user.set_password(newPassword)
        current_user.save()
        login(request, current_user)
        return redirect('home')
        