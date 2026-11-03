from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    print('HOME PAGE')
    return HttpResponse('HOME PAGE DO APP 1')