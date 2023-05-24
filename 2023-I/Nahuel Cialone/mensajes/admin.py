from django.contrib import admin

from .models import Conversacion, Mensaje

admin.site.register(Conversacion)
admin.site.register(Mensaje)
