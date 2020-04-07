from django.urls import paths
from . import views


urlpatterns = [
    path('^/$', views.hom)
]