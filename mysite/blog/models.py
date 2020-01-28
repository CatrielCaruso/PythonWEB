from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Usuario(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=10, help_text= "El usuario debe contener entre 6 a 10 caracteres")
    contrasenia = models.CharField(max_length=20, help_text= "La contraseña debe contener entre 8 a 16 caracteres")
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.TextField()

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True) #AutoField es un campo autoincremental 
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    descripcion = models.TextField()
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=100)
    dni= models.ForeignKey('Usuario', on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto') #Se pone asi cuando hay una relacion de muchos a muchos



