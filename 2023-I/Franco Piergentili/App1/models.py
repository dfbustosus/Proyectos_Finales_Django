from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class producto(models.Model):
    nombre= models.CharField(max_length=40)
    cantidad= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - cantidad {self.cantidad}"

class cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class proveedor(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Cuit {self.cuit}"

    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    cuit= models.IntegerField ()

from django.contrib.auth.models import User
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

