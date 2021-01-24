from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from new_app.models import Topic, Message
from new_app.serializers import TopicSerializer, MessageSerializer, \
    UserProfileSerializer


class TopicView(ListCreateAPIView):
    queryset = Topic.objects.all().order_by('-data_create')
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title']


class MessageView(ListCreateAPIView):
    queryset = Message.objects.all().order_by('time_create')  # -time_create - новые вверху
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


class UserProfileView(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.queryset.get(id=self.request.user.id)

# request.query_params - параметры после /?  в запросе
# request.query_params['username'] - пример
