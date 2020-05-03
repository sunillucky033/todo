from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class memory(models.Model):
    content=models.TextField()
    date=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)