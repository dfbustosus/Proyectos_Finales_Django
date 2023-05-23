from django.urls import path
from .views import *

urlpatterns = [
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('mensajes/', mensajes, name='mensajes'),
    path('casilla_mensajes/', casilla_mensajes, name='casilla_mensajes'),
    path('mostrar_mensaje/<id>', mostrar_mensaje, name='mostrar_mensaje'),
    path('eliminar_mensaje/<id>', eliminar_mensaje, name='eliminar_mensaje'),
    path('responder_mensaje/<id>', responder_mensaje, name='responder_mensaje'),
]