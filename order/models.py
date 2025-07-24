from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()
from product.models import Product

# Create your models here.

class Basket(AbstractModel):

    user = models.ForeignKey(User, related_name='baskets', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.price()
        return total_price

    def __str__(self):
        return self.user.username
    

class BasketItem(AbstractModel):

    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def price(self):
        amount = self.product.price * self.quantity
        return amount

    def __str__(self):
        return self.product.title