from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receptor = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField()
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.mensaje