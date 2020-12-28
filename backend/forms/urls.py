from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from forms.views import UserView, MessageView, CheckUser

router = SimpleRouter()

router.register('api/users', UserView)
router.register('api/messages', MessageView)
router.register('api/check_user', CheckUser)

urlpatterns = [

]

urlpatterns += router.urls
