from django.db import models

# Create your models here.

class Producto(models.Model):
    categoria = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    def __str__(self):
        return f"Categoria: {self.categoria} - Nombre {self.nombre} - Precio {self.precio}"

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesion {self.profesion}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    categoria = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Categoria {self.categoria}"
