# Generated by Django 3.2.4 on 2021-07-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('app', '0004_auto_20210622_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='authentication.User'),
        ),
    ]
