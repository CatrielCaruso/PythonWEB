from django.db import models
from django.db.models import CharField
from django.utils import timezone





class Producto(models.Model):
    # AutoField es un campo autoincremental
    nombre = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    id_producto = models.AutoField(primary_key=True)
    

   # def __str__(self):
       # return self.nombre


class Pedido(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
   
    fecha_pedido = models.DateTimeField(default=timezone.now)
    estado = models.BooleanField()

    #def __str__(self):
       # return self.descripcion


