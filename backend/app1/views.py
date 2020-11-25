from django.shortcuts import render

from app1.models import SalesOrder


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})
# обязательные поля: request, template_name
# template_name - имя html шаблона, который должен быть отрендерен на эту страницу
# orders - некоторая переменная (словарь)
