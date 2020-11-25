from rest_framework.serializers import ModelSerializer

from app1.models import SalesOrder


# сериалайзер
class OrderSerializer(ModelSerializer):
    class Meta:  # мета-данные нашего класса
        model = SalesOrder
        fields = ['amount', 'description']
