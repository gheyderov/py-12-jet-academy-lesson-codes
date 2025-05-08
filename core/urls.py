from django.contrib import admin
from django.urls import path
from core.views import homepage, contact

urlpatterns = [
    path('', homepage, name = 'home'),  # www.example.com/
    path('contact/', contact, name = 'contact') # www.example.com/contact/
]