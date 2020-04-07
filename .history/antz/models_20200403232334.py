from django.db import models

class Brand(models.Model):
    name = models.charField(max_length=128)
    
class CarModel(models.Model):
    name = models.charField(max_length=128)
