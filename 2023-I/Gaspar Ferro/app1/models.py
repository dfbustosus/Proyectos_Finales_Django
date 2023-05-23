from django.db import models

# Create your models here.

class Facciones(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
class Hobbits(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - genero {self.genero} - profesion{self.profesion}"
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
class Elfo(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - genero {self.genero} - profesion{self.profesion}"
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
class Enano(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - genero {self.genero} - profesion{self.profesion}"
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
class Orco(models.Model):
    def __str__(self):
        return f"nombre:{self.nombre} - genero {self.genero} - profesion{self.profesion}"
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

class Inicio(models.Model):
    usuario = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
