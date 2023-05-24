from django.db import models

# en el minuto 01:20:16 de la clase 18 esplica como cambiar el tipo de imformacion a recibir en los datos de entratada i.e int, str etc
# Create your models here.
class Gasto(models.Model):
    fecha= models.DateField()
    renta= models.IntegerField()
    alimentacion= models.IntegerField()
    educacion= models.IntegerField()
    transporte= models.IntegerField()    
    bills= models.IntegerField()
    vestuario= models.IntegerField()
    recreacion= models.IntegerField()  
    otros= models.IntegerField()
    def __str__(self):
        return f"Fecha: {self.fecha} - Renta {self.renta} - Alimentacion {self.alimentacion} - Educacion {self.educacion}  - Transporte {self.transporte}  - Bills {self.bills}  - Vestuario {self.vestuario}  - Recreacion {self.recreacion}  - Otros {self.otros}"
class Ingreso(models.Model):
    fecha= models.DateField()
    salario= models.IntegerField()
    part_time= models.IntegerField()
    alquileres= models.IntegerField()    
    otros= models.IntegerField()  
    def __str__(self):
        return f"Fecha: {self.fecha} - Salario {self.salario} - Part_Time {self.part_time} - Alquileres {self.alquileres}  - Otros {self.otros}"  
class Trading(models.Model):
    fecha= models.DateField()
    cryptocurrency= models.IntegerField()
    acciones= models.IntegerField()
    otros= models.IntegerField()
    def __str__(self):
        return f"Fecha: {self.fecha} - Cryptocurrency {self.cryptocurrency} - Acciones {self.acciones} - Otros {self.otros}"
    

from django.contrib.auth.models import User
# Clase 24
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    

'''
# Chequear si todo esta correcto
-->python manage.py check App1 
Deberia salirte: System check identified no issues (0 silenced).

# Transformar modelos a bases de datos
-->python manage.py makemigrations

# Ya se tiene la BD pero hay que alimentarla
-->python manage.py sqlmigrate App1 0001
# 0001 es el numero de la migracion se necesita un formato de 4 digitos
# Tambien podrias hacer: python manage.py sqlmigrate App1 initial
# Esto te devolvera todas las sql para crear las tablas

# Hacer la migracion 
-->python manage.py migrate

# Vamos al terminal y hacemos esto:
-->python manage.py createsuperuser
# Ingresa usernmae, email adress y password dos veces
luego corremos el codigo para probarlo
-->python manage.py runserver
'''

