from django.urls import path
from .views import *

urlpatterns = [
    path('', User.as_view(), name="users"),
    path('create', CreateUser.as_view(), name="create_user"),
    path('update/<int:pk>', UpdateUser.as_view(), name="update_user"),
    path('delete/<int:pk>', DeleteUser.as_view(), name="delete_user"),
    
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('register', Register.as_view(), name="register_user"),
    path('register/4dm1n', RegisterAdmin.as_view(), name="register_4dm1n"),
    path('updateU', Update.as_view(), name="updateU"),
]