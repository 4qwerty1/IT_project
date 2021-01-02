from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import json

from new_app.models import Topic, Message
from new_app.serializers import UserRegistrationSerializer, TopicSerializer, GetMessages, CreateMessage


class UserList(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filter_fields = ['login']
    # # имеет смысл, кода ищем по двум полям и более
    # # (пример: имя автора книги встречается в названии другой книги)
    # search_fields = ['firs_name', 'last_name']  # .../api/users/?search=...
    # # sorting by ...
    # # ?ordering=price - сортировка цены по возрастанию
    # # ?ordering=-price - сортировка цены по убыванию
    # ordering_fields = ['login', 'first_name', 'last_name']  # .../api/users/?ordering=...


class ListUsers(ListAPIView):
    queryset = get_user_model().objects.all().filter(is_staff=False)
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]


class ListTopics(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]


class GetMessagesView(ListAPIView):
    serializer_class = GetMessages
    permission_classes = [IsAuthenticated]
    filter_fields = ['topic']

    def get_queryset(self):
        if 'topic' not in self.request.query_params:
            return None
        else:
            topic = self.request.query_params['topic']
            return Message.objects.all().filter(topic=topic).order_by('time_create')


class CreateMessageView(CreateAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateMessage


class LoadNewMessages(ListAPIView):
    serializer_class = GetMessages
    permission_classes = [IsAuthenticated]
    filter_fields = ['topic']

    def get_queryset(self):
        params = self.request.query_params
        if 'topic' not in params or 'last_message' not in params:
            return None
        else:
            topic = self.request.query_params['topic']
            start = self.request.query_params['last_message']
            queryset = Message.objects.all().filter(topic=topic).order_by('time_create')

            # GT >, LT <, GTE >=, LTE <=
            return queryset.filter(time_create__lt=start)


# todo сделать чтобы get_messages и load_new_messages работали с body запроса, а не с его параметрами

# request.query_params - параметры после /?  в запросе
# request.query_params['username'] - пример
