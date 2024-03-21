from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from bemtevi.views import ( login, login_func, cadastro, cadastro_user, home, perfil, 
                        novo_tweet, user_logout, like_view, tweets,
                        retweet_view, seguir_view, seguindo_view, 
                        seguidores_view, postar, tweetsPerfil, get_tweet
)


urlpatterns = [
    path('', login, name='login'),
    path('login_func/', login_func, name='login_func'),


    path('logout/', user_logout, name='logout'),

    path('tweets/', tweets, name='tweets'),
    path('get_tweet/<int:id_tweet>/', get_tweet, name='get_tweet'),
    path('tweetsPerfil/<str:username>/', tweetsPerfil, name='tweetsPerfil'),
    path('postar/', postar, name='postar'),



    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro_user/', cadastro_user, name='cadastro_user'),

    path('home/', home, name='home'),
    # path('home/comentario/<int:id_tweet>/', comentario, name='comentario'),

    path('<str:username>/', perfil, name='perfil'),
    path('tweet/novo_tweet/', novo_tweet, name='novo_tweet'),

    path('like_view/<int:id_tweet>/', like_view, name='like_view'),
    path('retweet_view/<int:id_tweet>/', retweet_view, name='retweet_view'),

    path('seguir/<int:id_seguir>/<str:pag>/', seguir_view, name='seguir_view'),

    path('<str:username>/seguindo/', seguindo_view, name='seguindo_view'),
    path('<str:username>/seguidores/', seguidores_view, name='seguidores_view'),

    # path('reset_password/', reset_password, name='reset_password'),
    # path('likes/', likes, name='likes'),
    # path('retweets/', retweets, name='retweets'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)