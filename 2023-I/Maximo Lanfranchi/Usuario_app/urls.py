from django.urls import path 
from Usuario_app import views 

urlpatterns=[
    path('login', views.login_request, name="Login"),
    path('register', views.register_request, name= 'register-page'),
    path('logout/',views.logout_request, name='Logout'),
    path('update', views.profile, name='Perfil'),
    path('info', views.perfil_info, name='Info'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'), 
    path('verAvatares', views.avatares_list, name="VerAvatares"),
    path('eliminarAvatar', views.avatares_borrar, name='EliminarAvatar'),
    
] 