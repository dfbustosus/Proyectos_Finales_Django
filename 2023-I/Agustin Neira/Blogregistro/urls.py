from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', perfil_usuario, name='perfil'),
    path('agregar_url/', agregar_url, name='agregar_url'),
    path('editar_usuario/', editar_usuario, name='editar_usuario'),
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar'),
    path('agregar_descripcion/', agregar_descripcion, name='agregar_descripcion'),
]