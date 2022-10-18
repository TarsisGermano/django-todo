from django.db import models

class Item(models.Model):
    content = models.TextField()

Class GameDev(models.Model):
    nome =  models.CharField(max_length = 255)
    data_nascimento = models.DateField()
    empresa = models.CharField(max_length = 255)

