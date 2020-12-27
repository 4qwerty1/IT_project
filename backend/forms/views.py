from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from forms.models import User, Message
from forms.serializers import UserSerializer, MessageSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['login']
    # имеет смысл, кода ищем по двум полям и более
    # (пример: имя автора книги встречается в названии другой книги)
    search_fields = ['firstName', 'lastName']  # .../api/users/?search=...
    # sorting by ...
    # ?ordering=price - сортировка цены по возрастанию
    # ?ordering=-price - сортировка цены по убыванию
    ordering_fields = ['login', 'firstName', 'lastName']  # .../api/users/?ordering=...


class MessageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filter_fields = ['login']


