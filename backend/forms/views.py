from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from forms.models import MyUser
from forms.serializers import UserSerializer


def register(request):
    return render(request, 'register.html')


class UserView(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username']


def save_user(request):
    return render(request, 'test.html')
