from django.contrib import admin
from order.models import Basket, BasketItem

# Register your models here.


admin.site.register(Basket)
admin.site.register(BasketItem)