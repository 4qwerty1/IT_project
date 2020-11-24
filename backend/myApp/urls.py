# backend/notes/urls.py
from rest_framework import routers
from .views import NoteViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'myApp', NoteViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls
