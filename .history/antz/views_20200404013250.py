from django.shortcuts import render
from django.http import HttpResponse as response
from dateti

def index(request):
    now = datetime.now()
    return response("<body>Hello World!</body>")
    
