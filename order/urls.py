from django.urls import path
from order.views import cart, update_item

urlpatterns = [
    path('cart/', cart, name = 'cart'),
    path('update-item/', update_item, name='update-item')
]