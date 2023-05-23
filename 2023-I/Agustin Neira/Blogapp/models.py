from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = RichTextUploadingField()
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='Img_Post')
    
    
    def __str__(self):
        return self.titulo



