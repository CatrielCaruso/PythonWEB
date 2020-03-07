from django.db import models
from django.db.models import CharField
from django.utils import timezone




<<<<<<< HEAD
=======
    def __str__(self):
        return self.title

class Usuario(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    usuario = models.CharField(max_length=10, help_text= "El usuario debe contener entre 6 a 10 caracteres")
    password = models.CharField(max_length=20, help_text= "La contraseña debe contener entre 8 a 16 caracteres")
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering= ['usuario', 'password']

    def __str__(self):
        return  '%s %s' %(self.usuario, self.password)
>>>>>>> e9c2331847f5cb999388f37371463aa16da53349

class Producto(models.Model):
    # AutoField es un campo autoincremental
    nombre = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    id_producto = models.AutoField(primary_key=True)
    

<<<<<<< HEAD
   # def __str__(self):
       # return self.nombre
=======
    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'
        ordering =['id_categoria']


class Producto(models.Model):
    codigo = models.AutoField(primary_key=True) #AutoField es un campo autoincremental 
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    descripcion = models.TextField()
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
>>>>>>> e9c2331847f5cb999388f37371463aa16da53349

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'
        ordering =['codigo']


class Pedido(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
   
    fecha_pedido = models.DateTimeField(default=timezone.now)
    estado = models.BooleanField()

<<<<<<< HEAD
    #def __str__(self):
       # return self.descripcion
=======
    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural= 'Pedidos'
        ordering =['fecha_pedido']
    
    def __str__(self):
        return self.estado
    
>>>>>>> e9c2331847f5cb999388f37371463aa16da53349


