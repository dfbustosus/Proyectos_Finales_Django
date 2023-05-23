from django.urls import path
from AppFinal import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('usuarios', views.usuarios, name="Usuarios"),
    path('vehiculos', views.vehiculos, name="Vehiculos"),
    path('comentarios', views.comentarios, name="Comentarios"),
    path('buscarusuario/', views.buscarusuario),
    path('buscarvehiculo/', views.buscarvehiculo),
    path('administrador/', views.administrador_menu, name="Administrador"),
    path('administradorusuario/', views.leerUsuarios, name="admin_user"),
    path('administradorvehiculo/', views.leerVehiculos, name="admin_vehicle"),
    path('administradorcomentario/', views.leerComentarios, name="admin_coment"),
    path('eliminarUsuario/<usuario_nombre>/', views.eliminarUsuario, name="delete_user"),
    path('eliminarVehiculo/<vehiculo_marca>/', views.eliminarVehiculo, name="delete_vehicle"),
    path('eliminarComentario/<texto_texto>/', views.eliminarComentario, name="delete_coment"),
    path('editarUsuario/<usuario_nombre>/', views.editarUsuario, name="edit_user"),
    path('editarVehiculo/<vehiculo_marca>/', views.editarVehiculo, name="edit_vehicle"),
    path('editarComentario/<texto_texto>/', views.editarComentario, name="edit_coment"),
    path('loginrequest', views.login_request, name="Login"),
    path('register', views.register, name= 'Register'),
    path('logout', LogoutView.as_view(template_name="AppFinal/logout.html"), name = 'Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('aboutme', views.aboutme, name="aboutme"),
]