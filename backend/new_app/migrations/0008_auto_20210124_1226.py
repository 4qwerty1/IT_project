# Generated by Django 3.1.3 on 2021-01-24 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0007_auto_20210124_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='data_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
