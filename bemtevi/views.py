from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from bemtevi.models import Tweet
from django.contrib.auth.models import User

def home(request):
    tweets = Tweet.objects.all().order_by('-data')

    return render(request, 'bemtevi/home.html', {'tweets': tweets})

# def login(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST['username']
#             password = request.POST['password']
            
#             print(username)
#             print(password)
            
#             messages.success(request, 'Login - Sucesso')
#             return redirect('index')
#         except Exception as e:
#             messages.error(request, 'Erro ao fazer login')
#             return redirect('login')
    
#     return render(request, 'bemtevi/login.html')

from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            print('------ 1 -----')
            
            print(username)
            print(password)

            # Autentica o usuário
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

            # Verifica se as senhas coincidem
            if password != repeat_password:
                messages.error(request, 'As senhas não coincidem')
                return redirect('register')

            # Cria um novo usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            
            user.first_name = name.split()[0]
            user.last_name = ' '.join(name.split()[1:])
            user.save()
            
            print('salvo')

            messages.success(request, 'Usuario Registrado - Sucesso')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Erro ao fazer registro')
    
    return render(request, 'bemtevi/register.html')


def index(request):
    tweets = Tweet.objects.all().order_by('-data')
    return render(request, 'bemtevi/index.html', {'tweets': tweets})


# def post(request):
#     if request.method == 'POST':
#         try:
#             print('aquiiiiiiiiiiiiiiii')
#             tweet = request.POST['new_tweet']
#             datetime = datetime.now

#             print(tweet)
#             print(datetime)

#             return redirect('index')
#         except:
#             return redirect('index')

import datetime

def post(request):
    if request.method == 'POST':
        try:
            print('aquiiiiiiiiiiiiiiii')
            tweet = request.POST['new_tweet']  # Use get para evitar exceções se a chave não existir

            print(tweet)

            novo_tweet = Tweet.objects.create(
                user=request.user,
                tweet=tweet,
                data=datetime.datetime.now()
            )

            print(f"Tweet criado: {novo_tweet}")

            return redirect('index', {'data': request})
        except Exception as e:
            print(f"Erro ao processar o post: {e}")
            # Considere adicionar uma mensagem de erro ou redirecionar para uma página de erro
            return redirect('index')

    # Considere redirecionar para uma página de erro se o método não for POST
    return redirect('index')