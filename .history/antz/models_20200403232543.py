from django.db import models

class CardBrand(models.Model):
    name = models.charField(max_length=128)
    
class CarModel(models.Model):
    name = models.charField(max_length=128)
    brand = models.ForeignKey(CarBrand, on_delete = models.CASCADE)

class Car(models.Model):
    name = models.charField(max_length=255)
    brand = models.ForeignKey(CarBrand, on_delete = models.CASCADE)
    model = models.ForeignKey(CarBrand, on_delete = models.CASCADE)