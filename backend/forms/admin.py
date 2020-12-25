from django.contrib import admin
from django.contrib.admin import ModelAdmin

from forms.models import User, Topic, Message

admin.site.register(Topic)


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('login', 'id', 'firstName', 'lastName')


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('sender', 'topic')
    list_filter = ('sender', 'topic')
