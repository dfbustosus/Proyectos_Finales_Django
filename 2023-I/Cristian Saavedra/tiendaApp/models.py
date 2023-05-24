from django.db import models
from django.db.models.base import Model


# Create your models here.


class Category(models.Model):
    id=models.AutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Products(models.Model):
    id=models.AutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    #clave foranea con marca
    categoria=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categorias_prod') 
    fecha_fabricacion=models.DateField(auto_now=True)
    imagen=models.ImageField(upload_to='productos', null=True) #null true pq ya hay productos cargados sin fotos. la carpeta
    #productos se crea sola al interior de la carpeta media creada en la raíz

    #para que los campos se muestren en modo escritura crear función __str__ dentro de la clase Producto
    def __str__(self):
        return self.nombre

#para saber si la bd funciona okey se instala una extensión (costado izquierdo visual y se escribe sql en el buscador)
opciones_consultas=[
    [0,'consulta'],
    [1,'reclamo'],
    [2,'sugerencia'],
    [3,'felicitaciones']
]
class Contact(models.Model):
    id=models.AutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):
        return self.nombre
