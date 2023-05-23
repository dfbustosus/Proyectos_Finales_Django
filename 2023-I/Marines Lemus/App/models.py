from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Correo")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    def __str__(self):
        return f"Nombre: {self.name} - Correo: {self.email} - Creado: {self.date_joined}"

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Precio")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Código producto")
    image = models.ImageField(upload_to='products/', verbose_name="Imagen", default='default_image.jpg')

    def __str__(self):
        return f"Nombre: {self.name} - Precio: {self.price} - Código Producto: {self.sku}"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

class Sellers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Correo")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    def __str__(self):
        return f"Nombre: {self.name} - Correo: {self.email} - Creado: {self.date_joined}"

    class Meta:
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"