from django.urls import path
from product.api.views import categories, ProductAPIView, producttags, ProductUpdateDeleteAPIView

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('products/', ProductAPIView.as_view(), name = 'products'),
    path('product/<int:pk>/', ProductUpdateDeleteAPIView.as_view(), name = 'product_update')
    # path('producttags/', producttags, name = 'producttags')
]