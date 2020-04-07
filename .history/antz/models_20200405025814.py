from django.db import models

class Car(models.Model):
    url = models.CharField(max_length=500, unique=True, default = "")
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    kilometer = models.IntegerField(default=0)
    year = models.IntegerField()
    