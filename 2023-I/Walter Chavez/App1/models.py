from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre= models.CharField(max_length=40)
    precio= models.IntegerField()

class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    
class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    curso= models.IntegerField()