from django.db import models

# Create your models here.
class Item (models.Model):
    i_name = models.CharField(max_length=200)
    i_desc = models.CharField(max_length=200)
    i_price = models.IntegerField()