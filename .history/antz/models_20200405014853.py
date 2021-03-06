from django.db import models

class CardBrand(models.Model):
    name = models.CharField(max_length=128)
    
class CarModel(models.Model):
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(CardBrand, on_delete = models.CASCADE)
    
class CarTrim(models.Model):
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(CardBrand, on_delete = models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete = models.CASCADE)

class Car(models.Model):
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(CardBrand, on_delete = models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete = models.CASCADE)
    price = models.IntegerField()
    kmeter = models.IntegerField(default=0)
    year = models.IntegerField()
    