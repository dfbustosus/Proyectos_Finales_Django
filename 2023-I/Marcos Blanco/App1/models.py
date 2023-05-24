from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
     imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
     def __str__(self):
         return f"{self.user} - {self.imagen}"
     
class Calificacion(models.Model):
    usuario= models.CharField(max_length=30)
    fecha= models.DateField()
    puntaje= models.CharField(max_length=1)
    comentario= models.CharField(max_length=140)
    def __str__(self):
        return f"Usuario: {self.usuario} - Fecha {self.fecha} - Puntaje{self.puntaje} - Comentario {self.comentario}"
   
class Descripcion(models.Model):
    acerca= models.CharField(max_length=140)
    def __str__(self):
        return f"Acerca: {self.acerca} "
      
class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    telefono= models.CharField(max_length=15)
    consulta= models.CharField(max_length=140)
    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} - Telefono{self.telefono} - Consulta {self.consulta}"
         