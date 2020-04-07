from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=50, unique=True, default = "N/A")

class CarModel(models.Model):
    name = models.CharField(max_length=50, default = "N/A")
    car_brand = models.ForeignKey(
        'CarBrand',
        on_delete=models.CASCADE,
        default=1
    )
    class Meta:
        unique_together = ('name', 'car_brand')

class CarTrim(models.Model):
    name = models.CharField(max_length=50, unique=True, default = "N/A")
    car_brand = models.ForeignKey(
        'CarBrand',
        on_delete=models.CASCADE,
        default=1
    )
    car_model = models.ForeignKey(
        'CarModel',
        on_delete=models.CASCADE,
        default=1
    )
    class Meta:
        unique_together = ('name', 'car_brand', 'car_model')

class URL(models.Model):
    url = models.CharField(max_length=500, unique=True, default="N/A")

class Car(models.Model):
    url = models.ForeignKey(
        'URL',
        on_delete=models.CASCADE,
    )
    car_brand = models.ForeignKey(
        'CarBrand',
        on_delete=models.CASCADE,
    )
    car_model = models.ForeignKey(
        'CarModel',
        on_delete=models.CASCADE,
    )
    car_trim = models.ForeignKey(
        'CarTrim',
        on_delete=models.CASCADE,
        null=True
    )
    price = models.IntegerField(null=True)
    kilometer = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    