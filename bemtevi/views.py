from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from bemtevi.models import ( Usuario, Tweet, Like,
                            Retweet, Seguidor )
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.shortcuts import render, redirect
import datetime
from bemtevi.utils import user_data_context

def index(request):
    tweets = Tweet.objects.all().order_by('-data')[:100]
    return render(request, 'bemtevi/index.html', {'tweets': tweets})


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            _username = '@'+username
            user = authenticate(request, username=_username, password=password)

            if user is not None:
                django_login(request, user)
                messages.success(request, 'Login - Sucesso')
                return redirect('home')
    
            else:
                print('Usuário não autenticado')
                messages.error(request, 'Nome de usuário ou senha incorretos')
                return redirect('?')

        except Exception as e:
            messages.error(request, 'Erro ao fazer login')
            return redirect('login')
    
    return render(request, 'bemtevi/login.html')


def reset_password(request):
    return render(request, 'bemtevi/forget_password.html')


def register(request):
    if request.method == 'POST':
        try:
            # User
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            repeat_password = request.POST.get('password2')

            # Usuario
            nome = request.POST.get('name')
            sobrenome = request.POST.get('lastname')
            data_nascimento = request.POST.get('data_nascimento')
            foto_perfil = request.FILES.get('foto_perfil')

            special_characters = '*&¨%$#@!'
            if any(char in special_characters for char in username):
                messages.error(request, 'Caracteres invalidos no username')
                return redirect('register')
            
            if password != repeat_password:
                messages.error(request, 'As senhas não coincidem')
                return redirect('register')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este nome de usuário já está em uso')
                return redirect('register')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Este e-mail já está em uso')
                return redirect('register')

            # Cria novo usuário
            _username = '@'+username
            user = User.objects.create_user(username=_username, password=password)
            usuario = Usuario.objects.create(user=user, nome=nome, sobrenome=sobrenome, data_nascimento=data_nascimento, email=email, foto_perfil=foto_perfil)
            messages.success(request, 'Usuário registrado com sucesso')

            return redirect('login')
        
        except Exception as e:
            # Em caso de qualquer exceção, exiba uma mensagem de erro genérica
            print(e)
            messages.error(request, 'Erro ao fazer o registro')

    return render(request, 'bemtevi/register.html')


@login_required(login_url='login')
def home(request):
    contexto = user_data_context(request)
    tweets = Tweet.objects.all().order_by('-data')
    
    if request.method == 'POST':
        tweet = request.POST.get('tweet')
        # contexto_user = user_data_context(request)
        
        user = User.objects.get(username=request.user)
        usuario = Usuario.objects.get(user=user)
        
        newTweet = Tweet.objects.create(user=user, usuario=usuario, tweet=tweet)
        
        tweets = Tweet.objects.all().order_by('-data')
        return render(request, 'bemtevi/home.html', {'data': contexto, 'tweets':tweets})

    return render(request, 'bemtevi/home.html', {'data': contexto, 'tweets':tweets})



