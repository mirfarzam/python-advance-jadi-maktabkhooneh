from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    path('predict/', views.predict),
    path('getbrands/', views.getBrands),
    path('getmodels/<int:brand_id>', views.getModels),
    path('gettrims/<int:model_id>', views.getTrims),
    path('getprice/', views.predictPrice),
    path('getcars/', views.searchByPrice)
]