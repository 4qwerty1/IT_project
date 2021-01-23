from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from new_app.models import Topic, Message


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'avatar', 'first_name', 'last_name', 'is_staff',)


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title',)


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('name', 'avatar', 'topic', 'text', 'time_create')
        extra_kwargs = {'topic': {'write_only': True}}


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'avatar')
