from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Debate(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tema = models.CharField(max_length=100)
    opinion = models.TextField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.tema}'

class Opinion(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name='opiniones')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.mensaje}'

class Comentario(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name='comentarios')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.contenido
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
