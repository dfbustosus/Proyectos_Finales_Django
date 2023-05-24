from django.contrib.auth.models import User
from django.db import models
from item.models import Item

#relacionamos item a traves de los usuarios, con fecha de creacion y modificacion de los msjs
class Conversacion(models.Model):
    item = models.ForeignKey(Item, related_name='conversacion', on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User, related_name='conversacion')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-modificado',)

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, related_name='mensajes', on_delete=models.CASCADE)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, related_name='mensajes_creados', on_delete=models.CASCADE)