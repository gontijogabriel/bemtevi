from django.db import models
from django.contrib.auth.models import User

class Tweets(models.Model):
    class Meta:
        verbose_name_plural = 'tweets'
    
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField()
    data = models.DateField()
    
    def __str__(self):
        return self.data
    