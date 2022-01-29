from django.shortcuts import render, redirect


# Importar el Modelo de Usuarios (User)
from django.contrib.auth.models import Group, User
#Importar librerias de validación
from django.contrib.auth import authenticate,logout,login
# importar libreria de decoradores que permite evitar el ingreso a páginas  restringidas
from django.contrib.auth.decorators import login_required, permission_required #Decoradores para restringuir acceso a las páginas


# Create your views here.


def index(request):
    return render(request,'core/index.html');