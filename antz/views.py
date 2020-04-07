from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as response
from datetime import datetime
from django.views.generic import TemplateView
from django.views import View
from antz.models import Car
from . import views
from antz.models import CarBrand, CarModel, CarTrim, URL, Car


def index(request, car_id):
    return response('<body>Car Id is : {}</body>'.format(1))
