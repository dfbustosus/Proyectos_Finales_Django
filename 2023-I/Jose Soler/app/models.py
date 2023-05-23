from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True # Modifica el email para q sea unico

# Create your models here.

class Individuo(models.Model):
    apellidos = models.CharField(max_length=200, null=False)
    nombres = models.CharField(max_length=200, null=False)
    fecha_nacimineto = models.DateField(auto_now_add=False, null=True)
    aprobado = models.BooleanField(null=True)
    visitas = models.IntegerField(null=True)
    creador = models.ForeignKey(
        User,
        related_name='individuos',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )    
    def __str__(self):
        return self.nombres
    class Meta:
        app_label: 'app'
# _____________________________________________
class Partido(models.Model):
    nombre = models.CharField(max_length=200, null=False, unique=True)
    visitas = models.IntegerField(null=True)
    creador = models.ForeignKey(
        User,
        related_name='partidos',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )
    def __str__(self):
        return self.nombre
    class Meta:
        app_label: 'app'
# _____________________________________________
class Afiliacion(models.Model):
    individuo_FK = models.ForeignKey(
        Individuo,
        related_name='afiliaciones',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )
    partido_FK = models.ForeignKey(
        Partido,
        related_name='afiliaciones',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )
    Fecha_ingreso = models.DateField(auto_now_add=False, null=True) # Ojo aqui con estos datos
    Fecha_salida = models.DateField(auto_now_add=False, null=True)
    aprobado = models.BooleanField(null=True)       
    class Meta:
        app_label: 'app'       
# _____________________________________________
class Proceso(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    fecha_inicio = models.DateField(auto_now_add=False, null=False)
    fecha_fin = models.DateField(auto_now_add=False, null=True)
    abierto = models.BooleanField(null=False)
    entidad = models.CharField(max_length=200, null=False)
    monto = models.IntegerField(null=True)
    comentarios = models.TextField(null=True)
    aprobado = models.BooleanField(null=True)
    visitas = models.IntegerField(null=True)
    creador = models.ForeignKey(
        User,
        related_name='procesos',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )    
    class Meta:
        app_label: 'app'       
# _____________________________________________

class Implicado(models.Model):
    afiliado_FK = models.ForeignKey(
        Afiliacion,
        related_name='implicados',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )
    proceso_FK = models.ForeignKey(
        Proceso,
        related_name='implicados',
        null=True, #Toca cambiarlo a False
        on_delete=models.PROTECT
    )
    fecha_fin = models.DateField(auto_now_add=False, null=True)    
    acusacion = models.BooleanField(null=True)
    pena = models.CharField(max_length=200, null=True)
    comentarios = models.TextField(null=True)