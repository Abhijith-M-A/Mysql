from django.db import models

# Create your models here.
class Billpayers(models.Model):
    temp2 = models.CharField(max_length=200)
    temp1 = models.CharField(max_length=200)

class Billnonpayers(models.Model):
    temp5 = models.CharField(max_length=200)

