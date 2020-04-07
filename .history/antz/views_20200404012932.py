from django.shortcuts import render
from django.http import HttpResponse as rep

def index(request):
    return "Hello World!"
    
