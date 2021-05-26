from django.db import models

# Create your models here.
class Item(models.Model):
    product_name_fr = models.CharField(max_length=200)
    brands = models.CharField(max_length=200)
