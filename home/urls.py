from django.urls import path
from django.contrib import admin
from home import views as home_views

urlpatterns = [
    path('', home_views.home_page),
]
