from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='icons', null=True, blank=True)

    def __str__(self):
        return f'Id {self.id}: {self.username}'


class Topic(models.Model):
    title = models.CharField(max_length=100, unique=True)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Id {self.id}: {self.title}'


class Message(models.Model):
    text = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # может ссылаться на удаленного пользователя?
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From: {self.sender.username}'

    def get_name(self):
        return self.sender.get_full_name()

    def get_avatar(self):
        if self.sender.avatar == '':
            return None
        return self.sender.avatar.url

