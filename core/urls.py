from django.urls import path
from core.views import homepage, contact, about

urlpatterns = [
    path('', homepage, name = 'home'),  # www.example.com/
    path('contact/', contact, name = 'contact'), # www.example.com/contact/
    path('about/', about, name = 'about')
]