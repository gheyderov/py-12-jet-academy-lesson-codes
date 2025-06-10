from django.urls import path
from product.views import shop_detail, ProductListView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name = 'shop'),
    path('shop/<int:pk>/', shop_detail, name = 'shop-detail'),
]