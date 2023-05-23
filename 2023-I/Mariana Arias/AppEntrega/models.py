from django.db import models
from django.contrib.auth.models import User

class Recetas(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}"
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    descripcion = models.TextField()
    
class Buscar (models.Model):
    nombre = models.CharField(max_length=200)
    
class NewsLetter (models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}"
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    
    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
