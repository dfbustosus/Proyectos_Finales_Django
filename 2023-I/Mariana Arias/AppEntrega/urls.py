from django.urls import path 
from AppEntrega import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.inicio, name ="Inicio"),
    path('recetas',login_required(views.recetas), name="Recetas"),
     path('busquedaReceta',views.busquedaReceta, name="busquedaReceta"),
    path('buscar',views.buscar, name="Buscar"),
    path('newsletter',views.newsletter, name="NewsLetter"),
    path('leerRecetas',login_required(views.leerRecetas), name="LeerRecetas"),
    path('eliminarRecetas/<receta_nombre>/', login_required(views.eliminarRecetas), name="EliminarRecetas"),
    path('editarReceta/<receta_nombre>/', login_required(views.editarReceta), name="EditarRecetas"),
    path('login',views.login_request,name="Login"),
    path('register/',views.register,name="Register"),
    path('logout',LogoutView.as_view(template_name='AppEntrega/logout.html'),name='Logout'),
    path('editarPerfil',login_required(views.editarPerfil), name="EditarPerfil"), 
    path('agregarAvatar',login_required(views.agregarAvatar), name="AgregarAvatar"),
    path('aboutMe',views.aboutMe, name="AboutMe"),
   
    
]
