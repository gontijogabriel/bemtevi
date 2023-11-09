from django.urls import path
from bemtevi.views import login, login_senha

urlpatterns = [
    path('login/', login, name='login'),
    path('loginsenha/', login_senha, name='login-senha'),
]