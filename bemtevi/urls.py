from django.contrib import admin
from django.urls import path
from bemtevi.views import index, login, register, forget_password

urlpatterns = [
    path('bemtevi/', login, name='login'),
    path('forgetpassword/', forget_password, name='forget_password'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
]