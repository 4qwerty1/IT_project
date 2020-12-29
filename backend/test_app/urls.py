from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from test_app.views import TestUserView

urlpatterns = [
    url('auth/', include('djoser.urls')),
    url('auth/', include('djoser.urls.jwt')),
    url('test', TestUserView.as_view()),
]

