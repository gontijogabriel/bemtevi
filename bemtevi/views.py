from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from bemtevi.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.shortcuts import render, redirect

def home(request):
    tweets = Tweet.objects.all().order_by('-data')
    return render(request, 'bemtevi/index.html', {'tweets': tweets})

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


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    print('get register')
    if request.method == 'POST':
        print('post register')
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            repeat_password = request.POST.get('password2')

            # Verifica se as senhas coincidem
            if password != repeat_password:
                messages.error(request, 'As senhas não coincidem')
                return redirect('register')

            # Verifica se o usuário já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Este nome de usuário já está em uso')
                return redirect('register')

            # Verifica se o email já está em uso
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Este e-mail já está em uso')
                return redirect('register')

            # Cria um novo usuário
            # user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuário registrado com sucesso')
            return redirect('login')
        except Exception as e:
            # Em caso de qualquer exceção, exiba uma mensagem de erro genérica
            print(e)
            messages.error(request, 'Erro ao fazer o registro')

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