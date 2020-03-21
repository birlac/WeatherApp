from django.urls import path
from .import views
import requests

urlpatterns = [
    path('', views.hello, name='hello'),
    path('zip/', views.zip, name='ZipCode'),
    path('temp/', views.temp, name='Temperature'),
]