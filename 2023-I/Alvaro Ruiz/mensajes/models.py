from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensajeria(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    mensaje = models.TextField()
    horaDeEnvio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remitente} - {self.mensaje[:20]}"
    
