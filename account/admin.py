from django.contrib import admin
from account.models import User, BlockIpAdress

# Register your models here.

admin.site.register(User)
admin.site.register(BlockIpAdress)