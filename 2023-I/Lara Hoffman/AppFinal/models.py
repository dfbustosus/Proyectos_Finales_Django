from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STOCK_OPCIONES = [("disponible", "disponible"), ("no disponible", "no disponible")]
CATEGORIAS = [("Sillas de oficina", "Sillas de oficina"), ("Escritorios", "Escritorios")]

class Productos(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default="")
    descripcion = models.TextField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos") # ImageField si se instala Pillow
    stock = models.CharField(max_length=50, choices=STOCK_OPCIONES, default="disponible") # hay o no stock disponible
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"

class Mensajes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    comentario = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.nombre} dijo: {self.comentario}"

class Perfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # un usuario puede tener un solo perfil
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    descripcion = models.TextField(null=True , blank=True)
    link = models.URLField(max_length=200, null=True , blank=True)

    @staticmethod
    def get_or_create_perfil(user):
        perfil, created = Perfiles.objects.get_or_create(user=user)
        return perfil, created