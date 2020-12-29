from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    icon = models.ImageField(upload_to='icons', null=True, blank=True)

    # def clean_password(self):
    #     password = self.cleaned_data.get('password1')
    #     if len(password) < 8:
    #         raise ValidationError('Password too short')
    #     return super(MyUserCreationForm, self).clean_password1()

    def __str__(self):
        return f'Id {self.id}: {self.username}'
