from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class TestUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, response):
        return Response('ok')
