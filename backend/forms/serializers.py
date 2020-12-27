from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from forms.models import User, Message


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'firstname', 'lastname', 'icon')
