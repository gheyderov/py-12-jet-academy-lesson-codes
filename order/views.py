from django.shortcuts import render
from order.models import Basket, BasketItem
from django.http import JsonResponse
import json
from product.models import Product

# Create your views here.

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Product.objects.get(id = productId)

    basket, created = Basket.objects.get_or_create(user = request.user, is_active = True)
    basketItem, created = BasketItem.objects.get_or_create(basket = basket, product = product)

    if action == 'add':
        if not created:
            basketItem.quantity += 1
    if action == 'remove':
        basketItem.quantity -= 1

    basketItem.save()

    if basketItem.quantity <= 0:
        basketItem.delete()

    return JsonResponse('Item was added!', safe=False)

def cart(request):
    basket = Basket.objects.filter(user = request.user, is_active = True).first()
    context = {
        'basket' : basket
    }
    return render(request, 'cart.html', context)