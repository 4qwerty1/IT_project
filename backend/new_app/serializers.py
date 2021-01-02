from rest_framework.serializers import ModelSerializer, Serializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from new_app.models import Topic, Message


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'password', 'icon', 'first_name', 'last_name', 'is_staff', )


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class GetMessages(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'get_name', 'get_avatar', 'time_create')


class CreateMessage(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
