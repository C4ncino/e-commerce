from django.urls import path
from .views import *

urlpatterns = [
    path('', User.as_view(), name="users"),
    path('login_user', Login.as_view(), name="login"),
    path('logout_user', Logout.as_view(), name="logout"),
    path('register_user', Register.as_view(), name="register_user"),
]