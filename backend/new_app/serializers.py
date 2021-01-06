from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from new_app.models import Topic, Message


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'avatar', 'first_name', 'last_name', 'is_staff',)


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class GetMessages(ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'get_name', 'get_avatar', 'time_create')


class CreateMessage(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'avatar')
