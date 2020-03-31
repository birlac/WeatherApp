from django.urls import path
from .import views
import requests

urlpatterns = [
    path('', views.search, name='search'),
    path('zip/', views.zip, name='ZipCode'),
    path('temp/', views.temp, name='Temperature'),
    path('find/', views.find, name='find'),
    path('<int:city_id>', views.current, name='currentweather'),
]