from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    class Meta:
        verbose_name_plural = 'usuarios'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    @property
    def seguidores(self):
        return self.seguidores.all()
    
    @property
    def seguindo(self):
        return self.seguindo.all()
    
    @property
    def numero_seguidores(self):
        return self.seguidores.count()

    @property
    def numero_seguindo(self):
        return self.seguindo.count()
    
    @property
    def get_foto_perfil(self):
        return self.foto_perfil
    
    @property
    def sugestoes_para_seguir(self):
        usuarios_seguindo_ids = self.seguindo.values_list('seguidor__id', flat=True)
        sugestoes = Usuario.objects.exclude(id__in=usuarios_seguindo_ids).exclude(id=self.id)
        return sugestoes


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
    
    @property
    def user_has_liked(self):
        current_user = User.objects.get(username=self.user)
        return self.like_set.filter(user=current_user).exists()

    @property
    def user_has_retweeted(self):
        current_user = User.objects.get(username=self.user)
        return self.retweet_set.filter(user=current_user).exists()
    
    @property
    def get_total_likes(self):
        return self.like_set.count()

    @property
    def get_total_retweets(self):
        return self.retweet_set.count()

    
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

