from django.shortcuts import render
from django.http import HttpResponse as response


def index(request):
    now = datetime.now()
    return response("<body>Hello World!</body>")
    
