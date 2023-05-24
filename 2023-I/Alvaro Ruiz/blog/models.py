from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, null=True)
    contenido = models.TextField()
    fechaDePublicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images', null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

""" class PostImagen(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images', null=False)

    def __str__(self):
        return f"{self.post} - {self.imagen}" """

class Comentario(models.Model):
    nombreUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombreUsuario} - {self.post}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
