"""Definiuje wzorce adresó URL dla użytkowników"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #dołączenien domyślnych adresó URL uwirzytelnienia
    path('', include('django.contrib.auth.urls')),
    #strona rejestracji
    path('register/', views.register, name='register'),
]