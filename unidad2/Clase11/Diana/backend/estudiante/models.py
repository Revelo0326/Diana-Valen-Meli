from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=100)
    promedio = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

# Create your models here.
