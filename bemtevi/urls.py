from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from bemtevi.views import ( index, login, register, 
                            reset_password, home, likes,
                            newTweet
                        )

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('reset_password/', reset_password, name='reset_password'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('newTweet/', newTweet, name='newTweet'),
    path('likes/', likes, name='likes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)