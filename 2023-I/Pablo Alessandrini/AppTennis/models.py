from django.db import models


#  Defino los Models (Torneo/Jugador/Resultado)
class Torneo(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_jugadores = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10, unique=True, default='none')
    edad= models.PositiveIntegerField()
    telefono = models.CharField(max_length=30)
    comentario = models.TextField(default='')
    email = models.EmailField(max_length=144, default='')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Resultado(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    jugador1 = models.ForeignKey(Jugador, related_name="jugador1", on_delete=models.CASCADE)
    jugador2 = models.ForeignKey(Jugador, related_name="jugador2", on_delete=models.CASCADE)
    resultado = models.CharField(max_length=50)
    comentario = models.TextField(default='')

    def __str__(self):
        return f"{self.jugador1}  le gano por '{self.resultado}' a  {self.jugador2} en {self.torneo}"
 
class Inscripcion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Inscripcion de "{self.jugador.nombre} {self.jugador.apellido}" en el torneo: " {self.torneo.nombre} " '   