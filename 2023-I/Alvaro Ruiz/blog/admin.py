from django.contrib import admin
from .models import *
from mensajes.models import Mensajeria

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaDePublicacion',)
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Mensajeria)
admin.site.register(Comentario)
#admin.site.register(PostImagen)
admin.site.register(Post, PostAdmin)
admin.site.register(Avatar)