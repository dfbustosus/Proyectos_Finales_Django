from django.db import models

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    poster = models.ImageField(upload_to='imagenes_comidas/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre}'