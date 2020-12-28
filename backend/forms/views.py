from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from forms.models import User, Message
from forms.serializers import UserSerializer, MessageSerializer, ForGet

from django.http import HttpResponse
from django.views.generic import View


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer(fields=('id', 'login'))
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
    serializer_class = MessageSerializer(fields=('id', 'text'))

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return ForGet
    #     if self.action == 'list':
    #         return ForGet
    #     return ForGet


class CheckUser(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, **kwargs):
        login = request.query_params['login']
        password = request.query_params['password']

        if login is not None and password is not None:
            self.queryset = self.queryset.filter(login=login, password=password)

            return Response(True if self.queryset.count() == 1 else False)
