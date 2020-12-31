from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from forms.models import User
from forms.models import Message

from forms.serializers import UserSerializer
from forms.serializers import MessagesSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['login']


class MessagesView(ModelViewSet):
    queryset = Message.objects.all()

    # serializer_class = MessagesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['topic']

    def list(self, request):
        serializer = MessagesSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        return Response('create')
