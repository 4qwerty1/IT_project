from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    sex = models.BooleanField()
    favPL = models.CharField(max_length=50)
    favPattern = models.CharField(max_length=50)

    # для корректного отображения в админке
    def __str__(self):
        return f'Id {self.id}: {self.username}'
