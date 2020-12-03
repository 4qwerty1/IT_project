from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from app1.views import main_page, OrderView, orders_app

# router = DefaultRouter()

# router.register('orders', OrderView)

# urlpatterns = router.urls
