from django.shortcuts import render
from django.http import HttpResponse as response
from datetime import datetime

def index(request):
    now = datetime.now()
    return response(f"<body>Hello World! </body>")
    
