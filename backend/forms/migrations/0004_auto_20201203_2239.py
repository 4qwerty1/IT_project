# Generated by Django 3.1.3 on 2020-12-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20201203_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='favPL',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='favPattern',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='FavLang',
        ),
        migrations.DeleteModel(
            name='FavPattern',
        ),
    ]