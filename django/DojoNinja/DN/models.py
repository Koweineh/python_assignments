from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    State1 = models.CharField(max_length=255)
    
    
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojos = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    
