from django.db import models

class Usuario(models.Model):
    nombre =  models.CharField(max_length=100)
    correo =  models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    pin = models.CharField(max_length=4)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
# Create your models here.
