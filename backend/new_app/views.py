from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict

from backend.settings import SECRET_KEY
from new_app.models import Topic, Message
from new_app.serializers import UserRegistrationSerializer, TopicSerializer, MessageSerializer, \
    UserProfileSerializer
import jwt


class ListUsers(ListAPIView):
    queryset = get_user_model().objects.all().filter(is_staff=False)
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]


class TopicView(ListCreateAPIView):
    queryset = Topic.objects.all().order_by('-data_create')
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title']


class MessageView(ListCreateAPIView):
    queryset = Message.objects.all().order_by('time_create')  # time_create - новые внизу, -time_create - вверху
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MessageSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['topic']

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if 'last_message' in params:
            start = self.request.query_params['last_message']
            # GT >, LT <, GTE >=, LTE <=
            queryset = queryset.filter(time_create__gt=start)
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        token = self.request.headers['Authorization'].split()[1]
        user_id = jwt.decode(token, algorithms='HS256', key=SECRET_KEY)['user_id']
        return get_user_model().objects.get(id=user_id)

    def get(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(self.get_object())

        user = self.get_object()
        print(user.first_name)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()

        serializer = UserProfileSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# request.query_params - параметры после /?  в запросе
# request.query_params['username'] - пример
