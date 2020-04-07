from django.shortcuts import render
from django.http import HttpResponse as res

def index(request):
    return "Hello World!"
    
