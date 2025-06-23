from django.urls import path
from product.api.views import categories, products, producttags

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('products/', products, name = 'products'),
    # path('producttags/', producttags, name = 'producttags')
]