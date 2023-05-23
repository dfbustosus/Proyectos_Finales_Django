from django.urls import path
from .import views

app_name= 'app'

urlpatterns =[
    path('Home', views.index, name='index'), #Muestra Pag Principal
    path('Home_login_post', views.Home_login_post, name='Home_login_post'), # recoje los datos del login
    path('Home_registro_post', views.Home_registro_post, name='Home_registro_post'), # Recojer los datos del formulario
    path('Consul_List_Indi_Admin', views.Consul_Lista_Individuos_Admin, name='consu'),
    path('Pag_Admin', views.Pag_Admin, name='Pag_Admin'), # Pagina inicio de sesion Admin
    path('Pag_Usu', views.Pag_Usu, name='Pag_Usu'), # Pagina inicio de sesion Usuario
    path('', views.cerrar_sesion_post, name='cerrar_sesion_post'), # Boton cerrar sesion 
    path('Actualizar_Datos_Admin', views.Actualizar_Datos_Admin, name='Actualizar_Datos_Admin'), # Boton Actualizar Datos
    path('Actualizar_Datos_Post/<int:id_usuario>', views.Actualizar_Datos_Post, name='Actualizar_Datos_Post'), # Recoje Datos para actualizar
    path('Actualizar_Datos_Usu', views.Actualizar_Datos_Usu, name='Actualizar_Datos_Usu'), # Boton Actualizar Datos
    path('Crear_Partido_Politico', views.Crear_Partido_Politico, name='Crear_Partido_Politico'), # Boton Crear Partido Politico
    path('Crear_Partido_Politico_Post/<int:id_usuario>', views.Crear_Partido_Politico_Post, name='Crear_Partido_Politico_Post'), # Recoje Los Datos 
    path('Lista_Partido/<int:id_usuario>', views.Lista_Partido, name='Lista_Partido'), # Url Lista Partidos Admin
    path('Consular_PartidoP_Usuario',views.Consutar_PartidoP_Usuario,name='Consultar_Partido_Usuario'),#Url Consultar Partido
    path('Crear_Individuo_Admin',views.Crear_Individuo_Admin,name='Crear_Individuo_Admin'),#Boton Crear Individuo
    path('Crear_Individuo_Admin_Post/<int:id_usuario>', views.Crear_Individuo_Admin_Post, name='Crear_Individuo_Admin_Post'), # Recoje Los Datos 
    path('Crear_Individuo_Usu',views.Crear_Individuo_Usu,name='Crear_Individuo_Usu'),#Boton Crear Individuo
    path('Crear_Individuo_Usu_Post/<int:id_usuario>', views.Crear_Individuo_Usu_Post, name='Crear_Individuo_Usu_Post'), # Recoje Los Datos 
    #path('Lista_Individuo_Admin/<int:id_usuario>', views.Lista_Individuo_Admin, name='Lista_Individuo_Admin'), # Url Lista idivduos Admin
    path('Crear_Proceso_Admin',views.Crear_Proceso_Admin,name='Crear_Proceso_Admin'),#Boton Crear Proceso
    path('Crear_Proceso_Admin_Post', views.Crear_Proceso_Admin_Post, name='Crear_Proceso_Admin_Post'), # Recoje Los Datos
    path('Crear_Proceso_Usu',views.Crear_Proceso_Usu,name='Crear_Proceso_Usu'),#Boton Crear Proceso
    path('Crear_Proceso_Usu_Post/<int:id_usuario>', views.Crear_Proceso_Usu_Post, name='Crear_Proceso_Usu_Post'), # Recoje Los Datos
    path('Lista_Individuos/<int:id_usuario>', views.Lista_Individuos, name='Lista_Individuos'), # Url Lista idivduos Admin
]

