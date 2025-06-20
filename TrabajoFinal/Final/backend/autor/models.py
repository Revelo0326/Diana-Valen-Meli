from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"