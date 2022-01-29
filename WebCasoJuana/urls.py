from django.contrib import admin
from django.urls import path, include 
from .views import *
# De las views importamos los métodos para renderizar las páginas

urlpatterns = [
    path('',index,name='INDEX'),
    path('login/', registroCliente , name= 'LOGIN'),
    path('carrito/',cart,name='CART'),
    path('arrienda/',arrienda,name='ARRIENDA'),
    path('repara/',repara,name='REPARA'),
]