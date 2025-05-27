from django.shortcuts import render, get_object_or_404
from product.models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'shop.html', context)

def shop_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)
    context = {
        'product' : product
    }
    return render(request, 'shop-detail.html', context)