from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views


# urls que me van a dirigir a cada Template 
urlpatterns = [
    path('',views.inicio, name='inicio'),
   # path('Torneo/', views.torneo, name='torneo'),
    path('Jugador/', views.jugador, name='jugador'),
    path('Resultado/', views.resultado, name='resultado'),
    path('torneoFormulario/',views.torneoFormulario,name='TorneoFormulario'),
    path('jugadorFormulario/',views.jugadorFormulario,name='JugadorFormulario'),
    path('resultadoFormulario/',views.resultadoFormulario,name='ResultadoFormulario'),
    path('busquedaTorneo/', views.busquedatorneo, name='busquedaTorneo'),
    path('resultadoBusquedaTorneo/', views.buscar_torneo, name='resultadoBusquedaTorneo'),
    path('busquedaJugador/', views.busquedajugador, name='busquedajugador'),
    path('resultadoBusquedaJugador/', views.buscar_jugador, name='resultadoBusquedaJugador'),
    path('novedades/',login_required(views.novedades), name='novedades'),
    path('listadostorneos/', views.listadostorneos, name='listadostorneos'),
    path('sobre_mi/', views.sobremi, name='sobremi'),     
    path('contactanos/', views.contactanos, name='contactanos'),  
    path('lista_jugadores/', views.lista_jugadores, name='lista_jugadores'),  
    path('inscripciones/', views.inscripcionFormulario , name='inscripciones'),     
    path('lista_resultados/', views.lista_resultados, name='lista_resultados'),
    path('gestion_inscripcion/', views.leerinscripcion, name='gestion_inscripcion'), 
    path('gestion_jugador/', views.leerjugador, name='gestion_jugador'), 
    path('gestion_torneo/', views.leertorneo, name='gestion_torneo'), 
    path('gestion_resultado/', views.leerresultado, name='gestion_resultado'),   
    path('inscripciones/eliminar/<int:inscripcion_id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),        
    path('inscripciones/editar/<int:inscripcion_id>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('jugadores/eliminar/<int:jugador_id>/', views.eliminar_jugador, name='eliminar_jugador'),
    path('jugadores/editar/<int:jugador_id>/', views.editar_jugador, name='editar_jugador'),
    path('torneo/eliminar/<int:torneo_id>/', views.eliminar_torneo, name='eliminar_torneo'),
    path('torneo/editar/<int:torneo_id>/', views.editar_torneo, name='editar_torneo'),
    path('resultado/eliminar/<int:resultado_id>/', views.eliminar_resultado, name='eliminar_resultado'),
    path('resultado/editar/<int:resultado_id>/', views.editar_resultado, name='editar_resultado'),
    path('login/', auth_views.LoginView.as_view(template_name='AppTennis/login.html'), name='login'),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view(template_name="AppTennis/logout.html"), name="logout"),
    path('editarperfil/',views.editarperfil,name="editarperfil"),
    
    
]