from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    icon = models.ImageField(upload_to='icons', null=True, blank=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    # для корректного отображения в админке
    def __str__(self):
        return f'Id {self.id}: {self.login}'


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
        return f'From: {self.sender.login}'

    def firstname(self):
        return self.sender.firstName

    def lastname(self):
        return self.sender.lastName

    def icon(self):
        return self.sender.icon.url
