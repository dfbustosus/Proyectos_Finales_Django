from django.db import models

# Create your models here.
class Entradas(models.Model):
	titulo = models.CharField(max_length=50)
	subtitulo = models.TextField(max_length=400)
	cuerpo = models.CharField(max_length=50)
	fecha = models.CharField(max_length=50)
	imagen = models.URLField()
	autor = models.CharField(max_length=50)
	
	def _str_(self):
		return self.nombre

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
