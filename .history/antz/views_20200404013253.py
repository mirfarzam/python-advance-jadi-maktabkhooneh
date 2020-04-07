from django.shortcuts import render
from django.http import HttpResponse as response
from datetime import date

def index(request):
    now = datetime.now()
    return response("<body>Hello World!</body>")
    
