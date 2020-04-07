from django.shortcuts import render
from django.http import HttpResponse as response
from datetime import datetime
from django.views.generic import TemplateView


def index(request):
    now = datetime.now()
    return response('<body>Hello World! right now is {}</body>'.format(now))
    
def car(request, car_id):
    return response('<body>Car Id is : {}</body>'.format(car_id))


class AboutView(TemplateView):
    template_name = 'about.html'