from django.shortcuts import render, redirect
from django.http import HttpResponse
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



    

