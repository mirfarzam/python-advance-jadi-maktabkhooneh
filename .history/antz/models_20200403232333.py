from django.db import models

class Brand(models.Model):
    name = models.charField(max_length=128)
    
class Car(models.Model):
    name = models.charField(max_length=128)
