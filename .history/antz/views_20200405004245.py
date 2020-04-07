from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as response
from datetime import datetime
from django.views.generic import TemplateView
from django.views import View


def index(request):
    now = datetime.now()
    return response('<body>Hello World! right now is {}</body>'.format(now))
    
def car(request, car_id):
    car = get_object_or_404(Car, )


class AboutView(TemplateView):
    template_name = 'about.html'
    
class ProductView(View):
    def get(self):
        return response('<body>Car Id is : {}</body>'.format(car_id))