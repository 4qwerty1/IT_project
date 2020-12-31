from rest_framework.serializers import ModelSerializer

from forms.models import User
from forms.models import Message


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'firstname', 'lastname', 'icon')
