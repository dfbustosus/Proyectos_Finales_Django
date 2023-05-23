from django.views.generic.base import TemplateView
from App1 import views
from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path("admin/",admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('consejos',views.consejos,name="consejos"),
    path('register/',views.register,name="register"),
    path('miperfil',views.miperfil,name="miperfil"),
    path('editarPerfil',views.editarPerfil, name="editarPerfil"),
    path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),
    path('editarPerfil',views.editarPerfil,name='editarPerfil'),
    path('foro',views.foro,name="foro"),
    path('nuevodebate/', views.nuevo_debate, name='nuevodebate'),
    path('debatenuevoexitoso',views.debatenuevoexitoso,name='debatenuevoexitoso'),
    path('ver_debates/', views.ver_debates, name='ver_debates'),
    path('opinar_sobre_debate/<int:debate_id>/', views.opinar_sobre_debate, name='opinar_sobre_debate'),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('debate/<int:debate_id>/opiniones/', views.ver_opiniones, name='ver_opiniones'),
    path('opinion_exitosa',views.opinion_exitosa,name='opinionexitosa'),
]

    


    
   

