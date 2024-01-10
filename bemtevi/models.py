from django.db import models


class Tweet(models.Model):
    class Meta:
        verbose_name_plural = 'tweets'

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tweet = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return f'Tweet de {self.user}'
    
