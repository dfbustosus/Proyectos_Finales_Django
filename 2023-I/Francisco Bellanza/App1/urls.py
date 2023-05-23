from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView


urlpatterns= [

    path('',views.inicio, name='Inicio'),
    path('about',views.about, name='About'),
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'),name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('mas',views.mas,name='Mas'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('inicioBlog',views.inicio_blog,name='InicioBlog'),
    path('gastronomia',views.gastronomia,name='Gastronomia'),
    path('recetas',views.recetas,name='Recetas'),
    path('leerUsuarios',views.leerUsuarios,name='LeerUsuarios'),
]