from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField(upload_to='icons', null=True, blank=True)

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
    # может ссылатьс на удаленного пользователя?
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From: {self.sender.username}'

    def firstname(self):
        return self.sender.first_name

    def lastname(self):
        return self.sender.last_name

    def icon(self):
        return '../backend' + self.sender.icon.url
