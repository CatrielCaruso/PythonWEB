from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#class Usuario(models.Model):
    #dni = models.CharField(max_length=10, primary_key=True)
    #nombre = models.CharField(max_length=45)
    #apellido = models.CharField(max_length=45)
    #direccion = models.CharField(max_length=100)
    #usuario = models.CharField(max_length=10, help_text= "El usuario debe contener entre 6 a 10 caracteres")
    #password = models.CharField(max_length=20, help_text= "La contraseña debe contener entre 8 a 16 caracteres")
    #telefono = models.CharField(max_length=15)
    #email = models.EmailField()

    #class Meta:
        #verbose_name= 'Usuario'
        #verbose_name_plural = 'Usuarios'
        #ordering= ['usuario', 'password']


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.TextField()

    def __str__(self):
        return self.nombre
    


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    @property
    def imagenURL(self):
        try:
            url= self.imagen.url
        except:
            url= ''
        return url

class Pedido(models.Model):
    perfil= models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    orden_completa= models.BooleanField(default=False)
    
   #def get_cart_items(self):
        #return self.items.all()

    #def get_cart_total(self):
        #return sum([item.product.precio for item in self.items.all()]) #Obtiene el total de lo que se va agregando al pedido

    def __str__(self):
        return str(self.id)

    @property
    def get_pedido_total(self):
        orderitems = self.pedidoitems_set.all()
        total= sum([item.get_total for item in orderitems])
        return total

    @property
    def get_pedido_items(self):
        orderitems = self.pedidoitems_set.all()
        total= sum([item.cantidad for item in orderitems])
        return total 
    
class PedidoItems(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.precio * self.cantidad
        return total
    






