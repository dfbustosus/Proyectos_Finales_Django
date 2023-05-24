from django.urls import path
from .views import *
from mensajes.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', aboutMe, name='about'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),
    path('posts/', posts, name='posts'),
    path('posts/crear/', crear_post, name='crear_post'),
    path('posts/<int:post_id>/eliminar/', eliminar_post, name='eliminar_post'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/comentar/', crear_comentario, name='crear_comentario'),
    path('posts/<int:coment_id>/comentar/eliminar/', eliminar_comentario, name='eliminar_comentario'),
    path('perfil/', avatarPerfil, name='perfil'),
    path('perfil/editar/', editarPerfil, name="editar_perfil"),
    path('perfil/avatar/', agregarAvatar, name="agregar_avatar"), 
]
