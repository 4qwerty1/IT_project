from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from forms.views import register, UserView, save_user

router = SimpleRouter()

router.register('api/users', UserView)

urlpatterns = [
    path('', register),
    path('save_user', save_user),
]

urlpatterns += router.urls
