from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
    #Me permite agregar parametro de orden alfabetico
    class Meta:
        ordering = ('nombre',)
    
    #agregamos para poder ver nombres en la representacion de vista "admin"
    def __str__(self):
        return self.nombre
    
class Item(models.Model):
    #Puedo relacionar una categoria y agrupar los items, si se borra la categoria, se borran los items asociados
    categoria = models.ForeignKey(Categoria, related_name='items', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='item_imagen', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    #Puedo relacionar usuario y agruparlos en varios items, si se borra el creador, se borra el item con el cascade
    creador = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    creado_fecha = models.DateField(auto_now_add=True)
    
    #Me permite agregar parametro de orden alfabetico
    class Meta:
        ordering = ('nombre',)
        
    #agregamos para poder ver nombres en la representacion de vista "admin"
    def __str__(self):
        return self.nombre