from django.db import models

# Create your models here.
class Product(models.Model):
    product_name_fr = models.CharField(max_length=200)
    brands = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=1)
    stores = models.CharField(max_length=1000)
    url = models.CharField(max_length=2000)
