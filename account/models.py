from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    photo = models.ImageField('photo', upload_to='user_photos/', null=True, blank=True)
    phone = models.CharField('phone', max_length=100, null=True, blank=True)
    bio = models.TextField('bio', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True) # [127.9.9.1, 123.34.56.78]

    def get_profile_photo(self):
        if self.photo:
            return self.photo.url
        return '/static/images/profile.jpg/'
    

class BlockIpAdress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address