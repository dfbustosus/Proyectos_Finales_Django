from django.urls import path
# from django.conf.urls import handler404
from AppFinal import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about', views.about, name="About"),
    path('productos/list', views.ProductosList.as_view(), name="List"),
    path('<int:pk>', views.ProductosDetail.as_view(), name="Detail"),
    path('nuevo/', views.ProductosCreate.as_view(), name="New"),
    path('editar/<int:pk>', views.ProductosUpdate.as_view(), name="Edit"),
    path('borrar/<int:pk>', views.ProductosDelete.as_view(), name="Delete"),
    path('mensajes', views.mensajes, name="Mensajes"),
    path('leerMensajes', views.leerMensajes, name="LeerMensajes"),
    path('eliminarMensaje/<mensaje_nombre>', views.eliminarMensaje, name="EliminarMensaje"),
    path('editarMensajes/<mensaje_nombre>', views.editarMensaje, name="EditarMensaje"),
    path('buscar', views.buscar, name="Buscar"),
    path('login', views.login_request, name="Login"),
    path('registro', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppFinal/index.html'), name='Logout'),
    path('perfil', views.perfil, name="Perfil"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('<str:slug>/', views.error_404, name='error_404')

]
# handler404 = 'AppFinal.views.error_404'