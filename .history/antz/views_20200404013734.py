from django.shortcuts import render
from django.http import HttpResponse as response
from datetime import datetime

def index(request):
    now = datetime.now()
    return response('<body>Hello World! right now is {}</body>'.format(now))
    
def car(request, car_id):
    return response('<body>Car Id is : {}</body>'.format(car_id))
