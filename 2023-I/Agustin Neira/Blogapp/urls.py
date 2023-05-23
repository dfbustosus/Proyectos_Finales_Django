from django.urls import path
from .views import *
from django.contrib.auth. views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),

    # Funcionalidad de los posteos
    path('posteos', posteos, name='posteos'),
    path('nuevoPost/', postFormulario, name='nuevoPost'),
    path('lista_posteos/', lista_posteos, name='lista_posteos'),
    path('mostrarPost/<id>', mostrarPost, name='mostrarPost'),
    path('borrar_post/<id>', borrar_post, name='borrar_post'),
    path('editar_post/<id>', editar_post, name='editar_post'),

    path('about/', about, name='about'),
]