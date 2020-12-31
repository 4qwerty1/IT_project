from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from forms.views import UserView, MessageView, CheckUser
from test_app.views import TestUserView

router = SimpleRouter()

router.register('api/users', UserView)
# router.register('api/users', TestUserView.as_view())

router.register('api/messages', MessageView)
router.register('api/check_user', CheckUser)

urlpatterns = [
    # url('api/users', TestUserView.as_view()),
]

urlpatterns += router.urls
