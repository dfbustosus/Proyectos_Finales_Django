from django.urls import path 
from App1 import views 
from django.contrib.auth.views import LogoutView

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('contacto', views.contacto, name='Contacto'),
    path('productos', views.productos, name='Productos'),
    path('info', views.info, name='Info'),
    path('busquedaCurso',views.busquedaCurso,name="BusquedaCurso"),
    path('buscar/',views.buscar),
    path('login',views.login_request, name="Login"),
    path('login1',views.login1_request, name="Login1"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),
]
