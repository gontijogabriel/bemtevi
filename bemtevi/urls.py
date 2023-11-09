from django.urls import path
from bemtevi.views import login

urlpatterns = [
    path('login/', login, name='login'),
]