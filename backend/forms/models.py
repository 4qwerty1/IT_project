from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    sex = models.BooleanField()
    favPL = models.CharField()
    favPattern = models.CharField()
