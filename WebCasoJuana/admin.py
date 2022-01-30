from django.contrib import admin
from .models import *


class ReparacionAdmin(admin.ModelAdmin):
    list_display = ["reparacionID","nombres", "apellidos", "correo","marca_modelo","comentario","esAceptada"]  
    list_editable = ["nombres", "apellidos", "esAceptada"] 
    list_filter = ["reparacionID","nombres","apellidos","correo","marca_modelo","esAceptada"] 
    list_per_page = 5 
    search_fields = ["reparacionID","nombres","apellidos","correo","marca_modelo"]


# Register your models here.

    reparacionID = models.AutoField(primary_key = True)
    nombres = models.TextField(max_length= 100)
    apellidos = models.TextField(max_length = 100)
    correo = models.CharField(max_length= 40)
    marca_modelo = models.TextField(max_length= 100)
    comentario = models.TextField(max_length = 100)
    esAceptada = models.BooleanField(default = False)

admin.site.register(Reparacion,ReparacionAdmin)