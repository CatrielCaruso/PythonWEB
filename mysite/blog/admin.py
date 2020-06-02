from django.contrib import admin
from .models import  *


# Register your models here.


admin.site.register(Perfil)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(PedidoItems)
admin.site.register(Categoria)

