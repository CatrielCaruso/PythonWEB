from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as do_logout
from django.contrib.auth.decorators import login_required
from blog.models import Producto
from .forms import CreateUserForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@login_required
def home(request):
    # La logica deberia ser algo asi para obtener y compara con la base de datos y despueés ver como enviarlo a la template pedidos.
    # def home(request,id):
    # producto_seleccionado=producto.objects.get(id_producto=id)
    
    produ=Producto.objects.all()
    return render(request, 'blog/main.html',{"produ":produ})


@login_required
def producto(request):
    return render(request, 'blog/producto.html')



@login_required
def pedido(request):
    
    
    request.session["carrito"]
    print(request.session.get("carrito"))
    carrito=request.session.get("carrito")
    return render(request, 'blog/pedidos.html',{"carrito":carrito})  

@login_required
def index(request):
    request.session["carrito"]=[]
    print(request.session.session_key)
    return render(request, 'blog/index.html')

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


@login_required
def pedidos(request,id_producto): 
#def pedidos(request):
   
   pedi = Producto.objects.get(id_producto=id_producto)
   
  
   request.session["carrito"].append(pedi.descripcion)
   print(request.session.get("carrito"))
   
   
   print("carrito")

   produ=Producto.objects.all()
   return render(request, 'blog/main.html',{"produ":produ})


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
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


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

