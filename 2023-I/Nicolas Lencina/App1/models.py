from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=40)
    codigodeventa= models.IntegerField()
    descripcion= models.TextField(default='')
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    
    def __str__(self):
            return f"Producto: {self.nombre} - Código de venta {self.codigodeventa} - descripcion {self.descripcion} "




class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
