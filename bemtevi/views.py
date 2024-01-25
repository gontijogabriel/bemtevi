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
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.db.models import Count


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # print(
        #     f'{email}\n'
        #     f'{senha}\n'
        # )

        try:
            _username = User.objects.get(email=email)


            user = authenticate(request, username=_username.username, password=senha)

            if user is not None:
                django_login(request, user)
                messages.success(request, 'Login - Sucesso')
                return redirect('home')

            else:
                print('Usuário não autenticado')
                messages.error(request, 'Nome de usuário ou senha incorretos')
                return render(request, 'login.html')
            
        except Exception as e:
            messages.error(request, 'Erro ao fazer login')
            return render(request, 'login.html')


    return render(request, 'login.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        foto_perfil = request.FILES.get('foto_perfil')

        if senha != senha2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso. Por favor, escolha outro.')
            return render(request, 'cadastro.html')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este e-mail já está em uso. Por favor, escolha outro.')
            return render(request, 'cadastro.html')
        

        # Cria um novo usuário
        user = User.objects.create_user(username=username, email=email, password=senha)

        # Cria um novo usuário personalizado associado ao User criado acima
        usuario = Usuario.objects.create(
            user=user,
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            foto_perfil=foto_perfil
        )

        # print(
        #     f'{username}\n'
        #     f'{nome}\n'
        #     f'{sobrenome}\n'
        #     f'{email}\n'
        #     f'{senha}\n'
        #     f'{senha2}\n'
        #     f'{foto_perfil}\n'
        # )

        messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        return redirect('login')

    return render(request, 'cadastro.html')


@login_required(login_url='/')
def home(request):

    user = User.objects.get(username=request.user)
    usuario = Usuario.objects.get(user=user)

    contexto = {
        'id_user':user.pk,
        'username':user.username,
        'id':usuario.pk,
        'nome':usuario.nome,
        'sobrenome':usuario.sobrenome,
        'email':usuario.email,
        'foto':usuario.foto_perfil,
    }

    # tweets = Tweet.objects.all().order_by('-data')[:100]
    tweets = Tweet.objects.annotate(total_likes=Count('like'), total_retweets=Count('retweet')).order_by('-data')[:100]

    return render(request, 'home.html', {'data':contexto, 'tweets':tweets})


def perfil(request, username):
    
    user = User.objects.get(username=request.user)
    usuario = Usuario.objects.get(user=user)

    contexto = {
        'id_user':user.pk,
        'username':user.username,
        'id':usuario.pk,
        'nome':usuario.nome,
        'sobrenome':usuario.sobrenome,
        'email':usuario.email,
        'foto':usuario.foto_perfil,
    }

    tweets_user = Tweet.objects.filter(user=user).order_by('-data')[:100]

    return render(request, 'perfil.html', {'data':contexto, 'tweets':tweets_user})


from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

@login_required(login_url='/')
def novo_tweet(request):
    if request.method == 'POST':
        tweet_text = request.POST.get('tweet')
        user = request.user
        usuario = get_object_or_404(Usuario, user=user)
        
        new_tweet = Tweet.objects.create(user=user, usuario=usuario, tweet=tweet_text)

        return redirect('home')
            


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('login') 




# @login_required(login_url='login')
# def home(request):
#     contexto = user_data_context(request)
#     tweets = Tweet.objects.all().order_by('-data')
#     likes = Like.objects.all()
#     retweets = Retweet.objects.all()

#     for tweet in tweets:
#         tweet.liked_by_user = tweet.like_set.filter(user=request.user).exists() if request.user.is_authenticated else False
#         tweet.retweeted_by_user = tweet.retweet_set.filter(user=request.user).exists() if request.user.is_authenticated else False

#     # for tweet in tweets:
#     #     tweet.retweeted_by_user = tweet.retweet_set.filter(user=request.user).exists() if request.user.is_authenticated else False

#     print('chamou aq')
    
#     # if request.method == 'POST':
#     #     tweet = request.POST.get('tweet')
#     #     # contexto_user = user_data_context(request)
        
#     #     user = User.objects.get(username=request.user)
#     #     usuario = Usuario.objects.get(user=user)
        
#     #     newTweet = Tweet.objects.create(user=user, usuario=usuario, tweet=tweet)
        
#     #     tweets = Tweet.objects.all().order_by('-data')
#     #     likes = Like.objects.all()
#     #     for tweet in tweets:
#     #         tweet.liked_by_user = tweet.like_set.filter(user=request.user).exists() if request.user.is_authenticated else False
        
#     #     return render(request, 'bemtevi/home.html', {'data':contexto, 'tweets':tweets, 'likes':likes, 'user':request.user})

#     return render(request, 'bemtevi/home.html', {'data':contexto, 'tweets':tweets, 'user':request.user})



# def newTweet(request):
#     if request.method == 'POST':
#         tweet = request.POST.get('tweet')
#         # contexto_user = user_data_context(request)
        
#         user = User.objects.get(username=request.user)
#         usuario = Usuario.objects.get(user=user)
        
#         newTweet = Tweet.objects.create(user=user, usuario=usuario, tweet=tweet)

#         return redirect('home')
        


# @login_required(login_url='login')
# def likes(request):
#     if request.method == 'POST':
#         id_tweet = request.POST.get('id_tweet')
#         id_user = request.POST.get('id_user')

#         print(f'LIKE = id user: {id_user} / id tweet: {id_tweet}')
#         try:
#             user_data = User.objects.get(id=id_user)
#             tweet_data = Tweet.objects.get(id=id_tweet)

#             # Verifica se o usuário já deu like nesse tweet
#             existing_like = Like.objects.filter(user=user_data, tweet=tweet_data)

#             if existing_like.exists():
#                 # Se o like já existe, exclui
#                 existing_like.delete()
#                 print('like removido!')
#                 return redirect('home')

#             else:
#                 # Se o like não existe, cria
#                 user_like_tweet = Like.objects.create(user=user_data, tweet=tweet_data)
#                 print('like - ok!')

#                 return redirect('home')

            
#         except User.DoesNotExist or Tweet.DoesNotExist:
#         # Adicione um tratamento apropriado se o usuário ou tweet não existir
#             print('Erro: Usuário ou Tweet não encontrado.')
#         return redirect('home')
    

# @login_required(login_url='login')
# def retweets(request):
#     if request.method == 'POST':
#         id_tweet = request.POST.get('id_tweet')
#         id_user = request.POST.get('id_user')

#         print(f'RETWEET = id user: {id_user} / id tweet: {id_tweet}')
#         try:
#             user_data = User.objects.get(id=id_user)
#             tweet_data = Tweet.objects.get(id=id_tweet)

#             # Verifica se o usuário já deu like nesse tweet
#             existing_retweet = Retweet.objects.filter(user=user_data, tweet=tweet_data)

#             if existing_retweet.exists():
#                 # Se o like já existe, exclui
#                 existing_retweet.delete()
#                 print('retweet removido!')
#                 return redirect('home')

#             else:
#                 # Se o like não existe, cria
#                 user_retweet_tweet = Retweet.objects.create(user=user_data, tweet=tweet_data)
#                 print('retweet - ok!')

#                 return redirect('home')

            
#         except User.DoesNotExist or Tweet.DoesNotExist:
#         # Adicione um tratamento apropriado se o usuário ou tweet não existir
#             print('Erro: Usuário ou Tweet não encontrado.')
#         return redirect('home')
    
