from django.urls import path
from product.views import ProductDetailView, ProductListView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name = 'shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name = 'shop-detail'),
]