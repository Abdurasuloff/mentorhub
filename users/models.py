from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profile_images/", default='profile_images/default_pic.jpg')
    bio = models.CharField(max_length=200, null=True, blank=True)
    is_teacher = models.BooleanField(default=False)
    
 
    def __str__(self):
        return str(self.username)
    
    