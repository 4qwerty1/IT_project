from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from forms.views import UserView
from forms.views import MessagesView

router = SimpleRouter()

router.register('api/users', UserView)
router.register('api/messages', MessagesView)

urlpatterns = [

]

urlpatterns += router.urls
