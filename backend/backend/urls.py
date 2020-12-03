"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from app1.views import main_page, OrderView, orders_app

router = SimpleRouter()

# как правило все адресы для api инпоитов начинаяются с префикса 'api/orders'
router.register('api/orders', OrderView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),  # назначим на главную страницу сайта
    # path('orders_page/', include('app1.urls')), ТАК ДЕЛАЛ СТАС
    path('orders_page/', orders_app),
]

urlpatterns += router.urls  # router.urls - это список
