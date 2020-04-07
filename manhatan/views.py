from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse as response
from django.template import loader
from antz.models import CarBrand, CarModel, CarTrim, URL, Car
from django.http import JsonResponse
from django.core import serializers
from sklearn import linear_model
from django.views.decorators.csrf import csrf_exempt
from joblib import dump, load
import numpy as np

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return response(template.render(context, request))

def predict(request):
    template = loader.get_template('predictPrice.html')
    context = {}
    return response(template.render(context, request))

def search(request):
    template = loader.get_template('searchByPrice.html')
    context = {}
    return response(template.render(context, request))

def getBrands(request):
    brands = CarBrand.objects.all()
    result = []
    for brand in brands:
        result.append({'id':brand.id, 'name':brand.name})
    return JsonResponse({'brands' : result})


def getModels(request, brand_id):
    models = CarModel.objects.filter(car_brand_id = brand_id)
    result = []
    for model in models:
        result.append({'id': model.id, 'name': model.name})
    return JsonResponse({'models': result})

def getTrims(request, model_id):
    trims = CarTrim.objects.filter(car_model_id = model_id)
    result = []
    for trim in trims:
        result.append({'id': trim.id, 'name': trim.name})
    return JsonResponse({'models': result})

@csrf_exempt
def predictPrice(request):
    brand_id = int(request.POST.get('brand_id', 0))
    model_id = int(request.POST.get('model_id', 0))
    trim_id = int(request.POST.get('trim_id', 0))
    kilometer = int(request.POST.get('kilometer', 0))
    year = int(request.POST.get('year', 0))

    reg = linear_model.LinearRegression()
    reg = load('./manhatan/price_predicting_model.joblib')

    final = reg.predict(np.array([[brand_id, model_id, trim_id, year, kilometer]]))

    result = {
        'price' : round(final[0]/1000)*1000
    }
    return JsonResponse(result)


@csrf_exempt
def searchByPrice(request):
    max_price = int(request.POST.get('max_price', 0))
    min_price = int(request.POST.get('min_price', 0))
    cars = Car.objects.exclude(price__isnull=True).exclude(kilometer__isnull=True)
    if max_price > 0:
        cars = cars.filter(price__lte=max_price)
    if min_price > 0:
        cars = cars.filter(price__gte=min_price)
    cars = cars[:20]
    result = []
    for car in cars:
        temp_data = {
            'url' : car.url.url,
            'brand' : car.car_brand.name,
            'model' : car.car_model.name,
            'price' : car.price,
            'kilometer' : car.kilometer,
            'year' : car.year
        }
        result.append(temp_data)

    return JsonResponse({
        'cars' : result
    })