from django.contrib import admin
from django.urls import path

from main.views import SearchView


app_name = 'main'

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
]
