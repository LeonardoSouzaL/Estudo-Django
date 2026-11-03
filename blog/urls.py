from django.urls import path
from django.contrib import admin
from blog import views as blog_views


urlpatterns = [
    path('', blog_views.blog_page),

 ]
