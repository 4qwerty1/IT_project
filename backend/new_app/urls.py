from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from new_app.views import TopicView, MessageView, UserProfileView

router = SimpleRouter()

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/topics/', TopicView.as_view()),
    path('api/messages/', MessageView.as_view()),
    path('api/profile/', UserProfileView.as_view())
]

urlpatterns += router.urls
