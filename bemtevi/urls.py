from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from bemtevi.views import login, cadastro, home, perfil, novo_tweet, user_logout


urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('home/', home, name='home'),

    path('<str:username>/', perfil, name='perfil'),
    path('tweet/novo_tweet/', novo_tweet, name='novo_tweet'),

    # path('reset_password/', reset_password, name='reset_password'),
    # path('likes/', likes, name='likes'),
    # path('retweets/', retweets, name='retweets'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)