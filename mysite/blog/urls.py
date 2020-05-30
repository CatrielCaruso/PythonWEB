from django.urls import path, include
from . import views



urlpatterns = [
    
    path('', views.home, name='home'),
    path('pedido/', views.pedido, name='pedido'),
    path('update_item/', views.updateItem, name='update_item'),
    path('register/', views.register, name='register'),
    path('buscar/', views.buscar, name='buscar'),
    path('contacto/', views.contacto, name="contacto"),
    path('producto/', views.producto, name ='producto'),
    path('producto_filtrado/<pk>/', views.producto_filtrado, name='producto_filtrado'),
    path('finalizar_pedido/<id_pedido>/', views.finalizar_pedido, name='finalizar_pedido'),
    
    
    

]
