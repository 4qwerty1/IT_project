# Generated by Django 3.1.3 on 2021-01-02 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='icon',
            new_name='avatar',
        ),
    ]
