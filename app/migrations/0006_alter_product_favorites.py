# Generated by Django 3.2.4 on 2021-07-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('app', '0005_product_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorites',
            field=models.ManyToManyField(to='authentication.User'),
        ),
    ]