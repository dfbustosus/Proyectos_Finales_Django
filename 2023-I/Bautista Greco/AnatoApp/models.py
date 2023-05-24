from django.db import models



#####FALTA MAKEMIGRATIONS



# Create your models here.
    

class Asistencias(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - Comision: {self.comision} - Clase: {self.clase}"
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    clase = models.CharField(max_length=40)
    presente = models.BooleanField()


from django.contrib.auth.models import User

class Entrada(models.Model):
    def __str__(self):
        return f"Entrada: {self.titulo} - {self.autor} - {self.fecha}"
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media', null=True, blank = True) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  