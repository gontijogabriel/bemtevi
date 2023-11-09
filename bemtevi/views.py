from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def login_senha(request):
    return render(request, 'login_senha.html')
