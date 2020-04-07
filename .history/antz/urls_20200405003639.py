from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index),
    path('cars/<int:car_id>', views.car),
    path('about/', TemplateView.as_view(template_name="about.html"))
]