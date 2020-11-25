from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app1.models import SalesOrder
from app1.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


# обязательные поля: request, template_name
# template_name - имя html шаблона, который должен быть отрендерен на эту страницу
# orders - некоторая переменная (словарь)


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(request, 'main_app.html')
