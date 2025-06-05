from django.contrib import admin
from django.urls import path
from account.views import login, register, logout, profile

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('register/', register, name = 'register'),
    path('profile/', profile, name = 'profile'),
]