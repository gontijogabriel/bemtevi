from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            
            print(username)
            print(password)
            
            messages.success(request, 'Login - Sucesso')
            return redirect('index')
        except Exception as e:
            messages.error(request, 'Erro ao fazer login')
            return redirect('login')
    
    return render(request, 'bemtevi/login.html')


def forget_password(request):
    return render(request, 'bemtevi/forget_password.html')


def register(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            repeat_password = request.POST['repeatPassword']

            print(name)
            print(username)
            print(email)
            print(password)
            print(repeat_password)
            
            messages.success(request, 'Usuario Registrado - Sucesso')
            return redirect('index')
        except Exception as e:
            messages.error(request, 'Erro ao fazer registro')
            return redirect('login')
    
    return render(request, 'bemtevi/register.html')


def index(request):
    return render(request, 'bemtevi/index.html')