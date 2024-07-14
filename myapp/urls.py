# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),  # Define the chat URL pattern
]
