from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from new_app.views import ListUsers, ListTopics, GetMessagesView, CreateMessageView, LoadNewMessages

router = SimpleRouter()
# router.register('test', CreateMessageView)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/users', ListUsers.as_view()),
    path('api/topics', ListTopics.as_view()),
    re_path(r'^api/get-messages/$', GetMessagesView.as_view()),
    path('api/create-message', CreateMessageView.as_view()),
    re_path(r'^api/load-messages/$', LoadNewMessages.as_view()),

    # re_path(r'^api/users/(?P<pk>[^/.]+)/$', ListUsers.as_view()),
]

urlpatterns += router.urls
