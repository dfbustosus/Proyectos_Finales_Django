from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"
    






# Create your models here.
