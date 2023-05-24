from django.db import models

# Create your models here.

##clase cliente para guardar datos de clientes de la empresa##
class cliente(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    email=models.EmailField()
    contraseña=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Email: {self.email}"
    
##clase materiales para guardar datos de materiales de venta de la empresa##
class stock(models.Model):
    producto=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    def __str__(self):
        return f"{self.producto} {self.cantidad} - {self.precio}"

##clase para compra de productos##
class CompraUsuario(models.Model):
    usuario=models.CharField(max_length=20)
    producto=models.CharField(max_length=20)
    cantidad=models.IntegerField()



