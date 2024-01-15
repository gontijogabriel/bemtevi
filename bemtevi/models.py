from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    class Meta:
        verbose_name_plural = 'usuarios'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Tweet(models.Model):
    class Meta:
        verbose_name_plural = 'tweets'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tweet = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    comentario = models.BooleanField(default=False)

    def __str__(self):
        return f'Tweet de {self.user}'

    
class Like(models.Model):
    class Meta:
        verbose_name_plural = 'likes'

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like de {self.user} no tweet {self.tweet}'


class Retweet(models.Model):
    class Meta:
        verbose_name_plural = 'retweets'
        
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Retweet de {self.user} no tweet {self.tweet}'


class Seguidor(models.Model):
    class Meta:
        verbose_name_plural = 'seguidores'

    usuario = models.ForeignKey(Usuario, related_name='seguindo', on_delete=models.CASCADE)
    seguidor = models.ForeignKey(Usuario, related_name='seguidores', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seguidor} segue {self.usuario}'
