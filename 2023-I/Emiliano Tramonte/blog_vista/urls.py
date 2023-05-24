from django.urls import path 
from blog_vista import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('inicio/', views.InicioView.as_view(), name='inicio'),
    path('about/', views.about, name='About'),
    path('medicina/', login_required(views.medicina), name='Medicina'),
    path('miembros/', login_required(views.miembros), name='Miembros'),
    path('biologia/', login_required(views.biologia), name='Biologia'),
    path('filosofia/', login_required(views.filosofia), name='Filosofia'),
    path('astronomia/', login_required(views.astronomia), name='Astronomia'),
    path('tecnologia/', login_required(views.tecnologia), name='Tecnologia'),
    path('medicina/list', views.MedicinaList.as_view(), name='MedicinaList'),
    path('medicina/detalle/<int:pk>', views.MedicinaDetalle.as_view(), name='MedicinaDetail'),
    path('astronomia/list', views.AstronomiaList.as_view(), name='AstronomiaList'),
    path('astronomia/detalle/<int:pk>', views.detalle_astronomia, name='AstronomiaDetail'),
    path('filosofia/list', views.FilosofiaList.as_view(), name='FilosofiaList'),
    path('filosofia/detalle/<int:pk>', views.detalle_filosofia, name='FilosofiaDetail'),
    path('biologia/list', views.BiologiaList.as_view(), name='BiologiaList'), 
    path('biologia/detalle/<int:pk>', views.detalle_biologia, name='BiologiaDetail'),
    path('tecnologia/list', views.TecnologiaList.as_view(), name='TecnologiaList'),
    path('tecnologia/detalle/<int:pk>', views.detalle_tecnologia, name = 'TecnologiaDetail'),
    path('miembros/list', views.MiembrosList.as_view(), name='MiembrosList'),
    path('miembros/detalle/<int:pk>', views.MiembrosDetalle.as_view(), name='MiembrosDetail'),
    path('miembrosForm', views.miembros_form, name = 'MiembrosForm'),
    path('medicinaForm', views.medicina_form, name ='MedicinaForm' ),
    path('biologiaForm', views.biologia_form, name ='BiologiaForm' ),
    path('astronomiaForm', views.astronomia_form, name ='AstronomiaForm' ),
    path('filosofiaForm', views.filosofia_form, name ='FilosofiaForm' ),
    path('tecnologiaForm', views.tecnologia_form, name ='TecnologiaForm' ),
    path('miembros/editar/<int:pk>', views.MiembrosUpdate.as_view(), name='MiembrosEdit'),
    path('miembros/borrar/<int:pk>', views.MiembrosDelete.as_view(), name='MiembrosDelete'),
    path('medicina/editar/<int:pk>', views.MedicinaUpdate.as_view(), name='MedicinaEdit'),
    path('medicina/borrar/<int:pk>', views.MedicinaDelete.as_view(), name='MedicinaDelete'),
    path('astronomia/editar/<int:pk>', views.AstronomiaUpdate.as_view(), name='AstronomiaEdit'),
    path('astronomia/borrar/<int:pk>', views.AstronomiaDelete.as_view(), name='AstronomiaDelete'),
    path('biologia/editar/<int:pk>', views.BiologiaUpdate.as_view(), name='BiologiaEdit'),
    path('biologia/borrar/<int:pk>', views.BiologiaDelete.as_view(), name='BiologiaDelete'),
    path('filosofia/editar/<int:pk>', views.FilosofiaUpdate.as_view(), name='FilosofiaEdit'),
    path('filosofia/borrar/<int:pk>', views.FilosofiaDelete.as_view(), name='FilosofiaDelete'),
    path('tecnologia/editar/<int:pk>', views.TecnologiaUpdate.as_view(), name='TecnologiaEdit'),
    path('tecnologia/borrar/<int:pk>', views.TecnologiaDelete.as_view(), name='TecnologiaDelete'),
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='blog_vista/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('profile', login_required(views.profile), name='Profile'),
    path('inicio_login', login_required(views.inicio_login), name = 'InicioLogin'),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),

]




    

