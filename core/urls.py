from django.urls import path
from core.views import homepage, ContactView, about, export_view

urlpatterns = [
    path('', homepage, name = 'home'),  # www.example.com/
    path('contact/', ContactView.as_view(), name = 'contact'), # www.example.com/contact/
    path('about/', about, name = 'about'),
    path('export/', export_view, name = 'export')
]