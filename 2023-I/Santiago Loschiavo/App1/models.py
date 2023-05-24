from django.db import models


class Productos(models.Model):
    nombre= models.CharField(max_length=40)
    precio= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio {self.precio}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    puesto= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Puesto {self.puesto}"
    
class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    telefono= models.IntegerField()

"""from django.views.generic import ListView
class CursoList(ListView):
    model =Curso 
    template_name='/app1/curso_list.html'"""
