from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin', admin.site.urls),
    path('Home/', views.Home, name='Home'),
    path('', login_required(views.index), name='index'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_estudiante/', views.agregar_estudiante,name='agregar_estudiante'),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('agregar_entregable/', views.agregar_entregable,name='agregar_entregable'),
    path('buscar/', views.buscar, name='buscar'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('estudiante/<int:estudiante_id>/',views.detalle_estudiante, name='detalle_estudiante'),
    path('profesor/<int:profesor_id>/',views.detalle_profesor, name='detalle_profesor'),
    path('entregable/<int:entregable_id>/',views.detalle_entregable, name='detalle_entregable'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_request, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('Home/', views.Home, name='Home'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
    path('editar_avatar/', views.agregarAvatar, name='editar_avatar'),
    path('about_me/', views.about_me, name='about_me'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
