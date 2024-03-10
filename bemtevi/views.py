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
from django.contrib.auth import logout
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404


def login(request):
    return render(request, 'login/login.html')


def login_func(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        _username = User.objects.get(email=email)
        user = authenticate(request, username=_username.username, password=password)

        if user is not None:
            django_login(request, user)
            return JsonResponse({'message': 'Login bem-sucedido'}, status=200)
        else:
            return JsonResponse({'message': 'Credenciais inválidas'}, status=400)




@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('login')


def cadastro(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     nome = request.POST.get('nome')
    #     sobrenome = request.POST.get('sobrenome')
    #     email = request.POST.get('email')
    #     senha = request.POST.get('senha')
    #     senha2 = request.POST.get('senha2')
    #     foto_perfil = request.FILES.get('foto_perfil')

    #     if foto_perfil == None:
    #         foto_perfil = 'perfil/perfil_padrao.jpg'

    #     if senha != senha2:
    #         messages.error(request, 'As senhas não coincidem.')
    #         return render(request, 'cadastro.html')
        
    #     if Usuario.objects.filter(email=email).exists():
    #         messages.error(request, 'Este e-mail já está em uso. Por favor, escolha outro.')
    #         return render(request, 'cadastro.html')


    #     if User.objects.filter(username=username).exists():
    #         messages.error(request, 'Este e-mail já está em uso. Por favor, escolha outro.')
    #         return render(request, 'cadastro.html')

    #     user = User.objects.create_user(username=username, email=email, password=senha)
    #     usuario = Usuario.objects.create(
    #         user=user,
    #         nome=nome,
    #         sobrenome=sobrenome,
    #         email=email,
    #         foto_perfil=foto_perfil
    #     )
    #     print(
    #         f'{username}\n'
    #         f'{nome}\n'
    #         f'{sobrenome}\n'
    #         f'{email}\n'
    #         f'{senha}\n'
    #         f'{senha2}\n'
    #         f'{foto_perfil}\n'
    #     )
    #     messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
    #     return redirect('login')

    return render(request, 'cadastro/cadastro.html')


@login_required(login_url='/')
def home(request):
    print(request.user)
    # user = User.objects.get(username=request.user)
    # usuario = Usuario.objects.get(user=user)

    # usuarios_para_seguir = Usuario.objects.filter(~Q(seguidores__seguidor=usuario) & ~Q(user=user))
    
    # contexto = {
    #     'id_user': user.pk,
    #     'username': user.username,
    #     'id': usuario.pk,
    #     'nome': usuario.nome,
    #     'sobrenome': usuario.sobrenome,
    #     'email': usuario.email,
    #     'foto': usuario.foto_perfil,
    #     'para_seguir': usuarios_para_seguir,
    # }


    # tweets = Tweet.objects.annotate(total_likes=Count('like'), total_retweets=Count('retweet')).order_by('-data')[:100]
    # tweets_with_like_info = []

    # for tweet in tweets:
    #     user_has_liked = tweet.like_set.filter(user=user).exists()
    #     user_has_retweeted = tweet.retweet_set.filter(user=user).exists()

    #     tweet_info = {
    #         'tweet': tweet,
    #         'user_has_liked': user_has_liked,
    #         'user_has_retweeted': user_has_retweeted,
    #     }

    #     tweets_with_like_info.append(tweet_info)

    # return render(request, 'home.html', {'usuario': usuario, 'data': contexto, 'tweets': tweets_with_like_info})
    return render(request, 'home/home.html')


@login_required(login_url='/')
def perfil(request, username):
    user = User.objects.get(username=username)
    usuario = Usuario.objects.get(user=user)

    seguindo_ou_sim_nao = Seguidor.objects.filter(usuario=request.user.id, seguidor=usuario.id).exists()

    contexto = {
        'username_logado':str(request.user),
        'id_user':user.pk,
        'username':user.username,
        'id':usuario.pk,
        'nome':usuario.nome,
        'sobrenome':usuario.sobrenome,
        'email':usuario.email,
        'foto':usuario.foto_perfil,
        'seguidores': usuario.numero_seguidores,
        'seguindo': usuario.numero_seguindo,
        'seguindo_ou_sim_nao': seguindo_ou_sim_nao,
    }
    tweets = Tweet.objects.filter(usuario=usuario).annotate(total_likes=Count('like'), total_retweets=Count('retweet')).order_by('-data')[:100]
    tweets_with_like_info = []

    for tweet in tweets:
        user_has_liked = tweet.like_set.filter(user=user).exists()
        user_has_retweeted = tweet.retweet_set.filter(user=user).exists()

        tweet_info = {
            'tweet': tweet,
            'user_has_liked': user_has_liked,
            'user_has_retweeted': user_has_retweeted,
        }

        tweets_with_like_info.append(tweet_info)

    return render(request, 'perfil.html', {'usuario': usuario, 'data': contexto, 'tweets': tweets_with_like_info})

@login_required(login_url='/')
def novo_tweet(request):
    if request.method == 'POST':
        tweet_text = request.POST.get('tweet')
        user = request.user
        usuario = get_object_or_404(Usuario, user=user)
        new_tweet = Tweet.objects.create(user=user, usuario=usuario, tweet=tweet_text)
        return redirect('home')
            

@login_required(login_url='/')
def like_view(request, id_tweet):
    id_user = request.user.id

    try:
        user_data = User.objects.get(id=id_user)
        tweet_data = Tweet.objects.get(id=id_tweet)
        existing_like = Like.objects.filter(user=user_data, tweet=tweet_data)
        if existing_like.exists():
            existing_like.delete()
            print('like removido!')
            return redirect('home')
        else:
            user_like_tweet = Like.objects.create(user=user_data, tweet=tweet_data)
            print('like - ok!')
            return redirect('home')
    except User.DoesNotExist or Tweet.DoesNotExist:
        print('Erro: Usuário ou Tweet não encontrado.')
    return redirect('home')


@login_required(login_url='/')
def retweet_view(request, id_tweet):
    id_user = request.user.id
    try:
        user_data = User.objects.get(id=id_user)
        tweet_data = Tweet.objects.get(id=id_tweet)

        existing_retweet = Retweet.objects.filter(user=user_data, tweet=tweet_data)

        if existing_retweet.exists():
            existing_retweet.delete()
            print('retweet removido!')
            return redirect('home')
        else:
            user_retweet_tweet = Retweet.objects.create(user=user_data, tweet=tweet_data)
            print('retweet - ok!')
            return redirect('home')

    except User.DoesNotExist or Tweet.DoesNotExist:
        print('Erro: Usuário ou Tweet não encontrado.')
    return redirect('home')


@login_required(login_url='/')
def seguir_view(request, id_seguir):
    id_user = request.user.id
    try:
        user = Usuario.objects.get(id=id_user)
        seguir = Usuario.objects.get(id=id_seguir)
        existing_follow = Seguidor.objects.filter(usuario=user.id, seguidor=seguir.id)
        if existing_follow.exists() == False:
            follow = Seguidor.objects.create(usuario=user, seguidor=seguir)
            return redirect('home')
        else:
            existing_follow.delete()
            return redirect('home')

    except Exception as e:
        print(f'Erro view: seguir_view = {e}')
        return redirect('home')



@login_required(login_url='/')
def seguindo_view(request, username):
    usuario_logado = request.user
    user = User.objects.get(username=username)
    usuario = Usuario.objects.get(user=user)
    seguindo_ou_sim_nao = Seguidor.objects.filter(usuario=usuario_logado.id, seguidor=usuario.id).exists()

    # Obter os usuários que o usuário atual está seguindo
    usuarios_seguindo = [seguidor.seguidor.user for seguidor in usuario.seguindo.all()]

    # Obter os seguidores do usuário atual
    seguidores = [seguidor.usuario.user for seguidor in usuario.seguidores.all()]

    contexto = {
        'username_logado': str(usuario_logado),
        'id_user': user.pk,
        'username': user.username,
        'id': usuario.pk,
        'nome': usuario.nome,
        'sobrenome': usuario.sobrenome,
        'email': usuario.email,
        'foto': usuario.foto_perfil,
        'nm_seguidores': usuario.numero_seguidores,
        'nm_seguindo': usuario.numero_seguindo,
        'seguindo_ou_sim_nao': seguindo_ou_sim_nao,
        'seguindo': [{'username': usuario_seguindo.username, 'foto_perfil': usuario_seguindo.usuario.foto_perfil} for usuario_seguindo in usuarios_seguindo],
        'seguidores': [{'username': seguidor.username, 'foto_perfil': seguidor.usuario.foto_perfil} for seguidor in seguidores],
    }
    return render(request, 'seguindo.html', {'data': contexto})




@login_required(login_url='/')
def seguidores_view(request, username):
    usuario_logado = request.user
    user = User.objects.get(username=username)
    usuario = Usuario.objects.get(user=user)
    seguindo_ou_sim_nao = Seguidor.objects.filter(usuario=usuario_logado.id, seguidor=usuario.id).exists()

    # Obter os usuários que o usuário atual está seguindo
    usuarios_seguindo = [seguidor.seguidor.user for seguidor in usuario.seguindo.all()]

    # Obter os seguidores do usuário atual
    seguidores = [seguidor.usuario.user for seguidor in usuario.seguidores.all()]

    contexto = {
        'username_logado': str(usuario_logado),
        'id_user': user.pk,
        'username': user.username,
        'id': usuario.pk,
        'nome': usuario.nome,
        'sobrenome': usuario.sobrenome,
        'email': usuario.email,
        'foto': usuario.foto_perfil,
        'nm_seguidores': usuario.numero_seguidores,
        'nm_seguindo': usuario.numero_seguindo,
        'seguindo_ou_sim_nao': seguindo_ou_sim_nao,
        'seguindo': [{'username': usuario_seguindo.username, 'foto_perfil': usuario_seguindo.usuario.foto_perfil} for usuario_seguindo in usuarios_seguindo],
        'seguidores': [{'username': seguidor.username, 'foto_perfil': seguidor.usuario.foto_perfil} for seguidor in seguidores],
    }
    return render(request, 'seguidores.html', {'data': contexto})


def comentario(request, id_tweet):
    print(id_tweet)

    tweet = Tweet.objects.get(id=id_tweet)
    print(tweet.usuario.foto_perfil)

    return render(request, 'comentario.html', {'tweet': tweet})