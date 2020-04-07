from django.db import models

class Car(models.Model):
    url = models.TextField(unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=50, nullable=T)
    price = models.IntegerField()
    kilometer = models.IntegerField(default=0)
    year = models.IntegerField()
    