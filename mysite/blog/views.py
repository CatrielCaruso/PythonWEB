from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as do_logout
from django.contrib.auth.decorators import login_required
from blog.models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import json


# Create your views here.

@login_required
def home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context={'productos':productos, 'categorias':categorias}
    return render(request, 'blog/main.html',context)


@login_required
def pedido(request):
    perfil = request.user.perfil
    pedido, creado = Pedido.objects.get_or_create(perfil=perfil, orden_completa=False)
    items = pedido.pedidoitems_set.all()
    context={'items':items, 'pedido':pedido}
    return render(request, 'blog/pedidos.html',context) 

from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    perfil = request.user.perfil
    producto = Producto.objects.get(id=productId)
    pedido, creado = Pedido.objects.get_or_create(perfil=perfil, orden_completa=False)
    pedidoItem, creado =  PedidoItems.objects.get_or_create(pedido=pedido, product=producto)

    if action == 'add':
      pedidoItem.cantidad = (pedidoItem.cantidad + 1)
    elif action == 'remove':
      pedidoItem.cantidad = (pedidoItem.cantidad - 1)

    pedidoItem.save()

    if pedidoItem.cantidad <= 0:
      pedidoItem.delete()

    return JsonResponse('Articulo añadido al pedido', safe=False)



@login_required
def producto(request):
    return render(request, 'blog/producto.html')

@login_required
def producto_filtrado(request, pk=None):
    id = Categoria.objects.get(id_categoria=pk)
    cat_pro = Producto.objects.filter(id_categoria=id)
    return render(request, 'blog/producto_filtrado.html', {'cat_pro':cat_pro})
 

@login_required
def buscar(request):
    if request.GET["pro"]:

        #mensaje = " Articulo buscado:%r" % request.GET["pro"]
        producto = request.GET["pro"]
        articulos = Producto.objects.filter(descripcion__icontains=producto)

    return render(request, 'blog/producto.html', {"articulos": articulos, "query": producto})
    #else:

       # mensaje = "No has introducido ningun articulo"

    #return HttpResponse(mensaje)

def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
           
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
# def post_list(request):



@login_required
def contacto(request):
    if request.method=="POST":
       subject=request.POST["asunto"] 
       message=request.POST["mensaje"] + " " + request.POST["email"]
       email_from=settings.EMAIL_HOST_USER
       recipient_list=["cardozocaruso@gmail.com"]
       send_mail(subject,message,email_from,recipient_list)
    return render(request, 'blog/contacto.html')

