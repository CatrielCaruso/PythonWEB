from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout as do_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
#La logica deberia ser algo asi para obtener y compara con la base de datos y despueés ver como enviarlo a la template pedidos.    
#def home(request,id):
    #producto_seleccionado=producto.objects.get(id_producto=id)
    
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


