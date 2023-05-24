from django.urls import path
from .views import *

urlpatterns = [
    path('', progreso, name='lista_conversaciones'),
    path('enviar/', progreso, name='enviar_mensajes'),
    path('chat/', progreso, name='detalle_conversaciones'),
]