from django.urls import path
from core.views import homepage, ContactView, about

urlpatterns = [
    path('', homepage, name = 'home'),  # www.example.com/
    path('contact/', ContactView.as_view(), name = 'contact'), # www.example.com/contact/
    path('about/', about, name = 'about')
]