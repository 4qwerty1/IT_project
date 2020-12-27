from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from forms.views import UserView, MessageView

router = SimpleRouter()

router.register('api/users', UserView)
router.register('api/messages', MessageView)

urlpatterns = [

]

urlpatterns += router.urls
