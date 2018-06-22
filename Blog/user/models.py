from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname =models.CharField(max_length=50,blank=True)

    class Meta(AbstractUser.Meta):
        pass

class Addinfo(models.Model):
    nickname =models.CharField(max_length=50,blank=True)
    username =models.CharField(max_length=50,blank=True)


