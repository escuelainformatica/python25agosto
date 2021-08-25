from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()

# id = models.IntegerField() (ya esta agregado)
# por defecto, el id, es un campo numerico y se autoicrementa.
