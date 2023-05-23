from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home-page'),
    path('inicio', views.avatar, name="home-inicio"),
    path('mensajes/', views.mensaje_lista, name='mensaje_lista'),
    path('mensajes/nuevo/', views.mensaje_nuevo, name='mensaje_nuevo'),
    path('mensajes/<int:destinatario_id>/', views.mensaje_conversacion, name='mensaje_conversacion'),
    path('mensajes/eliminar/<int:mensaje_id>/', views.mensaje_eliminar, name='eliminar_mensaje'),
    
] 