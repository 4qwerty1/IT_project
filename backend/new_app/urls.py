from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from new_app.views import ListUsers, TopicView, MessageView, LoadNewMessages, UserProfileView

router = SimpleRouter()

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/users/', ListUsers.as_view()),
    path('api/topics/', TopicView.as_view()),
    path('api/messages/', MessageView.as_view()),
    re_path(r'^api/load-messages/$', LoadNewMessages.as_view()),
    path('api/profile/', UserProfileView.as_view())
]

urlpatterns += router.urls
