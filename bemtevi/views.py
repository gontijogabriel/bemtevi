from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from bemtevi.models import Tweet
from django.contrib.auth.models import User

def home(request):
    tweets = Tweet.objects.all().order_by('-data')

    return render(request, 'bemtevi/home.html', {'tweets': tweets})

from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print('ok')
                print('Usuário autenticado com sucesso, faz o login')
                django_login(request, user)
                messages.success(request, 'Login - Sucesso')
                return redirect('index')
            else:
                print('Usuário não autenticado')
                messages.error(request, 'Nome de usuário ou senha incorretos')
                return redirect('login')

        except Exception as e:
            messages.error(request, 'Erro ao fazer login')
            return redirect('login')
    
    return render(request, 'bemtevi/login.html')


def reset_password(request):
    return render(request, 'bemtevi/forget_password.html')


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            repeat_password = request.POST['repeatPassword']
            
            print(username)
            print(email)
            print(password)
            print(repeat_password)

            # Verifica se as senhas coincidem
            if password != repeat_password:
                messages.error(request, 'As senhas não coincidem')
                return redirect('register')

            # Cria um novo usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            print('salvo')

            messages.success(request, 'Usuario Registrado - Sucesso')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Erro ao fazer registro')
    
    return render(request, 'bemtevi/register.html')


def index(request):
    tweets = Tweet.objects.all().order_by('-data')[:100]
    return render(request, 'bemtevi/index.html', {'tweets': tweets})


import datetime
def post(request):
    if request.method == 'POST':
        try:
            tweet = request.POST['new_tweet']
            
            if tweet != '' and len(tweet) <= 256:
        
                novo_tweet = Tweet.objects.create(
                    user=request.user,
                    tweet=tweet,
                    data=datetime.datetime.now()
                )

                print(f"Tweet criado: {novo_tweet}")
                

            return redirect('index', {'data': request})
        
            
        except Exception as e:
            print(f"Erro ao processar o post: {e}")
            
            return redirect('index')
        
    return redirect('index')