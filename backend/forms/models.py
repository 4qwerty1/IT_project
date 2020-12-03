from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    sex = models.BooleanField()
    favPL = models.CharField(max_length=50)
    favPattern = models.CharField(max_length=50)


