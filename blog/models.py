from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class BlogCategory(AbstractModel):

    title = models.CharField('title', max_length=200)

    def __str__(self):
        return self.title
    

class Blog(AbstractModel):

    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=200)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='blog_images/')


    def __str__(self):
        return self.title
