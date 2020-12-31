from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model

from new_app.models import Topic, Message


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', )


admin.site.register(Topic)
admin.site.register(Message)

