from django.contrib import admin
from django.urls import path, include 
from .views import *
# De las views importamos los métodos para renderizar las páginas

urlpatterns = [
    path('',index,name='INDEX'),
    path('login/', cargaRegistro , name= 'LOGIN'),
    path('iniciar-sesion/',iniciarSesion,name='INICIAR_SESION'),
    path('registro/',registroCliente, name='REGISTRARSE'),
    path('cerrar-sesion/',cerrarSesion, name='LOGOUT'),
    path('carrito/',cart,name='CART'),
    path('arrienda/',arrienda,name='ARRIENDA'),
    path('repara/',repara,name='REPARA'),
    path('enviar-solicitud/',enviarConsulta,name='CONSULTA'),
    path('ver-solicitudes/',verConsultas, name='VER_CONSULTAS'),
]