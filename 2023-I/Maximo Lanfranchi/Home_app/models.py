from django.db import models
from django.contrib.auth.models import User


# Vacio

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.CharField(max_length=255)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente} a {self.destinatario}: {self.contenido}'
