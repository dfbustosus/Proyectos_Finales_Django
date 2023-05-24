from django.db import models

# Create your models here.
class Empleado(models.Model):
    dni=models.IntegerField()
    nombre= models.CharField(max_length=50)
    id_departamento=models.IntegerField()
    id_puesto=models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Departamento(models.Model):
    codigo=models.IntegerField()
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Puesto(models.Model):
    codigo=models.IntegerField()
    nombre= models.CharField(max_length=50)
    departamento=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.departamento}"