from django.db import models

# Create your models here.
class Pleet(models.Model):
    body = models.CharField(max_length=255)
    
    created_by = models.ForeignKey()