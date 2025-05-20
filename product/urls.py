from django.urls import path
from product.views import shop, shop_detail

urlpatterns = [
    path('shop/', shop, name = 'shop'),
    path('shop-detail/', shop_detail, name = 'shop-detail'),
]