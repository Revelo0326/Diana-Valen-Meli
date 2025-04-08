from django.db import models

class Clientes(models.Model):
    nombre =  models.CharField(max_length=100)
    apellido =  models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
# Create your models here.
