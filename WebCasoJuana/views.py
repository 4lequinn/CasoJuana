from django.shortcuts import render, redirect


# Importar el Modelo de Usuarios (User)
from django.contrib.auth.models import Group, User
#Importar librerias de validación
from django.contrib.auth import authenticate,logout,login
# importar libreria de decoradores que permite evitar el ingreso a páginas  restringidas
from django.contrib.auth.decorators import login_required, permission_required #Decoradores para restringuir acceso a las páginas

# Importamos los modelos 
from .models import *

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
            return render(request,"core/index.html")
        else:
            contexto = {"mensaje":"Correo electrónico o contraseña no válidos"}
            return render(request,'core/login.html',contexto)
    return render(request,'core/login.html')


@login_required(login_url='/login/')
def cerrarSesion(request):
    #Me cierra la sesión del usuario logeado en ese momento
    logout(request)
    return render(request,'core/index.html')

@login_required(login_url='/login/')
def arrienda(request):
    return render(request, 'core/arrienda.html');

@login_required(login_url='/login/')
def cart(request):
    return render(request, 'core/cart.html');

@login_required(login_url='/login/')
def repara(request):
    return render(request, 'core/repara.html');

@login_required(login_url='/login/')
@permission_required('WebCasoJuana.view_reparacion',login_url='/login/')
def verConsultas(request):
    mensaje = "Sin solicitudes."
    try:
        listaConsultas = Reparacion.objects.filter(esAceptada = False)
        datos = {"consultas":listaConsultas}
        return render(request,'core/ver-solicitudes.html',datos)
    except:
        datos = {"mensaje":mensaje}
        return render(request,'core/ver-solicitudes.html',datos)

@login_required(login_url='/login/')
def enviarConsulta(request):
    mensaje = "No enviado."
    if request.POST:
        # Recibimos los datos de la pagina
        nombres = request.POST.get("txtNombre")
        apellidos = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        marcaModelo = request.POST.get("txtMarca")
        comentario = request.POST.get("txtComentario")
        #esAceptada = request.POST.get("txtNombre")

        consulta = Reparacion(
            nombres = nombres,
            apellidos = apellidos,
            correo = correo,
            marca_modelo = marcaModelo,
            comentario = comentario,
            esAceptada = False
        )

        consulta.save()
        mensaje = "¡Enviado con éxito!"

    datos = {"mensaje":mensaje}

    return render(request, 'core/repara.html',datos)

@login_required(login_url='/login/')
@permission_required('WebCasoJuana.view_reparacion',login_url='/login/')
@permission_required('WebCasoJuana.change_reparacion',login_url='/login/')
def aceptarConsulta(request,id):
    listaConsultas = Reparacion.objects.all()
    # Obtengo la consulta seleccionada
    consulta = Reparacion.objects.get(reparacionID = id)
    consulta.esAceptada = True
    consulta.save()
    return redirect(to='VER_CONSULTAS')

@login_required(login_url='/login/')
@permission_required('WebCasoJuana.view_venta',login_url='/login/')
@permission_required('WebCasoJuana.change_venta',login_url='/login/')
def verInventario(request):
    return render(request, 'core/ver-inventario.html')

