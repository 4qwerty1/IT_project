from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.settings import SECRET_KEY
from new_app.models import Topic, Message
from new_app.serializers import UserRegistrationSerializer, TopicSerializer, GetMessages, CreateMessage, \
    UserProfileSerializer
import jwt


class ListUsers(ListAPIView):
    queryset = get_user_model().objects.all().filter(is_staff=False)
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]


class ListTopics(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GetMessagesView(ListAPIView):
    serializer_class = GetMessages
    permission_classes = [IsAuthenticatedOrReadOnly]
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
    permission_classes = [IsAuthenticatedOrReadOnly]
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
            return queryset.filter(time_create__gt=start)


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
