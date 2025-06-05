from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    photo = models.ImageField('photo', upload_to='user_photos/', null=True, blank=True)
    phone = models.CharField('phone', max_length=100, null=True, blank=True)
    bio = models.TextField('bio', null=True, blank=True)

    def get_profile_photo(self):
        if self.photo:
            return self.photo.url
        return '/static/images/profile.jpg/'