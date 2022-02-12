from pyexpat import model
from django.db import models

# Create your models here.
class usuarios(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contactmail = models.CharField(max_length=30)
    cellphone = models.PositiveIntegerField()
    
    