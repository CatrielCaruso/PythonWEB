from django.urls import path, include
from . import views



urlpatterns = [
<<<<<<< HEAD
    
    path('', views.home, name="home"),
    path('producto/', views.producto, name="producto"),
    path('pedidos/', views.pedidos, name="pedidos"),
    path('register/',views.register, name="register"),
    
    
  
    
    
   



]
=======
    #path('', views.post_list, name='post_list'),
    path('', views.inicio, name='inicio'),
    path('user/login/', views.login_user, name='login'),
]





>>>>>>> e9c2331847f5cb999388f37371463aa16da53349
