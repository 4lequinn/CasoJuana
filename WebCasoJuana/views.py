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

def cargaRegistro(request):
    return render(request, 'core/login.html');

def registroCliente(request):
    contexto = {"mensaje":""}
    if request.POST:
        # Guardamos en estas variables si el usuario envia por POST el formulario
        nom = request.POST.get("txtNombre")
        #ape = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        passw = request.POST.get("txtContraseña")
        try:
            #Buscará ese nombre de usuario en la tabla User
            #Si no lo encuentra entrará en el bloque exception
            usu = User.objects.get(username = correo)
            contexto = {"mensaje":"El Usuario ya se encuentra registrado!!"}
            return render(request,'core/login.html',contexto)
        except:
            usu = User()
            usu.first_name = nom
            #usu.last_name = ape
            usu.username = correo
            usu.email = correo
            usu.set_password(passw)
            usu.save()
            us = authenticate(request,username = correo,password = passw)
            login(request,us)
            contexto = {"mensaje":"Guardó el USUARIO CORRECTAMENTE"}
            return render(request,'core/index.html', contexto)

    return render(request, 'core/login.html');


# Método para iniciar sesión 
def iniciarSesion(request):
    if request.POST:
        usuario = request.POST.get("txtEmailLogin")
        password = request.POST.get("txtPassLogin")
        us = authenticate(request,username = usuario, password = password)

        if us is not None and  us.is_active:
            #Cargamos al usuario en todas las páginas
            login(request,us)
            print('YEEEEESS!')
            return render(request,"core/index.html")
        else:
            print('INVALIDO')
            contexto = {"mensaje":"Correo electrónico o contraseña no válidos"}
            return render(request,'core/login.html',contexto)
    return render(request,'core/login.html')


@login_required(login_url='/login/')
def cerrarSesion(request):
    #Me cierra la sesión del usuario logeado en ese momento
    logout(request)
    return render(request,'core/index.html')


def arrienda(request):
    return render(request, 'core/arrienda.html');

def cart(request):
    return render(request, 'core/cart.html');

def repara(request):
    return render(request, 'core/repara.html');