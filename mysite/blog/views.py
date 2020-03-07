from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout as do_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    
    return render(request, 'blog/main.html')

@login_required
def producto(request):
    return render(request, 'blog/producto.html')
@login_required
def pedidos(request):
    return render(request, 'blog/pedidos.html')


def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        username=form.cleaned_data['username']
        password=form.cleaned_data['password1']
        
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form= UserCreationForm()   

    context = {'form': form}
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'registration/register.html', context)

def logout(request):
     # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')    
# def post_list(request):


=======
from django.contrib.auth import authenticate, login
from .models import Usuario 



# Create your views here.
# def post_list(request):
#    return render(request, 'blog/post_list.html', {}) 

def inicio(request):
    return render(request, 'blog/inicio.html', {})

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse("Error al iniciar sesión")



    

>>>>>>> e9c2331847f5cb999388f37371463aa16da53349
