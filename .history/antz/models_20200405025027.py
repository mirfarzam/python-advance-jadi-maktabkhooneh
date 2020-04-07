from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField(unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=128)
    price = models.IntegerField()
    kmeter = models.IntegerField(default=0)
    year = models.IntegerField()
    