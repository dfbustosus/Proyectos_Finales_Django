from django.urls import path 
from app1 import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns=[

    #path('', views.Login_View, name="inicio"),
    path('crear', login_required(views.Faccion), name="crear"),
    path('hobbits', views.Crear_Hobbits, name="hobbits"),
    path('elfos', views.Crear_Elfos, name="elfos"),
    path('enanos', views.Crear_Enanos, name="enanos"),
    path('orcos', views.Crear_Orcos, name="orcos"),
   #path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(template_name='app1/logout.html'), name="logout"),
    path('', views.login_register_view, name='login_register'),
    path('pagina_gaspar', views.pagina_gaspar, name='pagina_gaspar'),
    path('leerelfos', views.leer_elfos, name="lectura_elfos"),
    path('leerenanos', views.leer_enanos, name="lectura_enanos"),
    path('leerorcos', views.leer_orcos, name="lectura_orcos"),
    path('leerhobbits', views.leer_hobbits, name="lectura_hobbits"),
    path('eliminar_elfo/<elfo_nombre>/', views.eliminar_elfo, name="eliminar_elfo"),
    path('eliminar_orco/<orco_nombre>/', views.eliminar_orco, name="eliminar_orco"),
    path('eliminar_enano/<enano_nombre>/', views.eliminar_enano, name="eliminar_enano"),
    path('eliminar_hobbit/<hobbit_nombre>/', views.eliminar_hobbit, name="eliminar_hobbit"),
    path('editar_elfo/<elfo_nombre>/', views.editar_elfo, name= "editar_elfo"),
    path('editar_enano/<enano_nombre>/', views.editar_enano, name= "editar_enano"),
    path('editar_hobbit/<hobbit_nombre>/', views.editar_hobbit, name= "editar_hobbit"),
    path('editar_orco/<orco_nombre>/', views.editar_orco, name= "editar_orco"),



]
