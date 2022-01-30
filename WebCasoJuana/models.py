from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


# Modelo formulario de reparacion de bicicleta

class Reparacion(models.Model):
    reparacionID = models.AutoField(primary_key = True)
    nombres = models.TextField(max_length= 100)
    apellidos = models.TextField(max_length = 100)
    correo = models.CharField(max_length= 40)
    marca_modelo = models.TextField(max_length= 100)
    comentario = models.TextField(max_length = 100)
    esAceptada = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.correo)

