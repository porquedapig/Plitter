from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PlitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    
    
    
User.plitter = property(lambda u:PlitterProfile.objects.get_or_create(user=u)[0])