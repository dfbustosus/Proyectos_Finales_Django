from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='Aca guardamos el tipo de archivo (MIME)')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'