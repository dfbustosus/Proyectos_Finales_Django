from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CARGO = "CA"
ELASTIZADO = "EL"
MOM = "MO"
WIDELEG = "WL" 
choicesPant = [
        (CARGO, "Cargo"),
        (ELASTIZADO, "Elastizado"),
        (MOM, "Mom"),
        (WIDELEG, "Wideleg"),]

class ProdRemera (models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=3)
    color = models.CharField(max_length=10)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Tamaño {self.tamaño} - Color {self.color} - Precio {self.precio} - Stock {self.stock}"

class ProdBuzo (models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=3)
    color = models.CharField(max_length=10)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Tamaño {self.tamaño} - Color {self.color} - Precio {self.precio} - Stock {self.stock}"

class ProdPantalon (models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=3)
    color = models.CharField(max_length=10)
    diseño = models.CharField(max_length=20, choices=choicesPant, default=CARGO)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Tamaño {self.tamaño} - Color {self.color} - Precio {self.precio} - Stock {self.stock}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Referencia a la estructura que almacena el usuario. El avatar se elimina junto al usuario.
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
