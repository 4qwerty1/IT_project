from django.contrib import admin

from forms.models import User, Topic, Message

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Message)

