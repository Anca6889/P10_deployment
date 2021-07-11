from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name_fr = models.CharField(max_length=200)
    brands = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=1)
    stores = models.CharField(max_length=1000)
    url = models.CharField(max_length=2000)
    image = models.TextField(default=None)
    categories = models.ManyToManyField(Category)
    favorites = models.ManyToManyField(User)

    def __str__(self):
        return self.product_name_fr
