from django.db import models

class Car(models.Model):
    url = models.CharField(max_length=500, unique=True, default = "N/A")
    brand = models.CharField(max_length=50, default = "N/A")
    model = models.CharField(max_length=50, default = "N/A")
    trim = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    kilometer = models.IntegerField(default=0)
    year = models.IntegerField()
    