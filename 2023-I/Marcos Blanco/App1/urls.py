from django.urls import path 
from App1 import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('', views.inicio, name="Inicio"),
     #path('Contactos', views.contactos, name="Contactos"),
     #path('Sugerencias', views.sugerencias, name="Sugernecias"),
     #path('Calificacion', views.calificacion, name="Calificacion"),
     path('getCalificacion', views.getCalificaciones, name="getCalificacion"),
     path('login',views.login_request, name="Login"),
     path('register', views.register, name='Register'),
     path('logout', LogoutView.as_view(template_name='App1/inicio.html'), name='Logout'),
     path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
     path('cambiarContraseña', views.cambiarContrasena, name="cambiarContraseña"),
     path('verPerfil', views.verPerfil, name="VerPerfil"),
    # path('Acerca', views.acerca, name="Acerca"),
    # path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('Calificacion',views.CalificacionList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.CalificacionDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.CalificacionCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CalificacionUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CalificacionDelete.as_view(),name='Delete'),
    #
    path('Acerca',views.DescripcionList.as_view(),name='DescList'),
    path(r'^(?P<pk>\d+)$', views.DescripcionDetalle.as_view(),name='DescDetail'),
    path(r'^Descnuevo$', views.DescripcionCreacion.as_view(),name='DescNew'),
    path(r'^Desceditar/(?P<pk>\d+)$',views.DescripcionUpdate.as_view(),name='DescEdit'),
    path(r'^Descborrar/(?P<pk>\d+)$',views.DescripcionDelete.as_view(),name='DescDelete'),
    #
    path('ContactosList',views.ContactoList.as_view(),name='ContList'),
    path(r'^(?P<pk>\d+)$', views.ContactoDetalle.as_view(),name='ContDetail'),
    path(r'^Contnuevo$', views.ContactoCreacion.as_view(),name='ContNew'),
    path(r'^Conteditar/(?P<pk>\d+)$',views.ContactoUpdate.as_view(),name='ContEdit'),
    path(r'^Contborrar/(?P<pk>\d+)$',views.ContactoDelete.as_view(),name='ContDelete'),
    path('exito', views.exito, name="Exito"),
    path('exitopass', views.exitopass, name="Exitopass"),




]     