from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class userinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    info=models.CharField(max_length=300)