from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog_page(request):
    print('BLOG PAGE')
    return HttpResponse("BLOG PAGE DO APP 1")