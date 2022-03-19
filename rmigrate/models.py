from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class A(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class B(models.Model):
    a = models.ForeignKey('A', on_delete=models.PROTECT)

class User(AbstractUser):
    pass
