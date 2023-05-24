from django.urls import path 
from App1 import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path,include


urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('Acceso', views.Acceso, name='Acceso'),
    path('Freelance', login_required(views.Freelance), name='Freelance'),
    path('Contratador',login_required(views.Contratador), name='Contratador'),
    path('Servicios',login_required(views.Servicios), name='Servicios'),
    path('contratadorFormulario', login_required(views.contratador_view), name='contratadorFormulario'),
    path('freelanceFormulario', login_required(views.freelance_view), name='freelanceFormulario'),
    path('serviciosFormulario', login_required(views.servicios_view), name='serviciosFormulario'),
    path('busquedaFreelance', views.busquedaFreelance, name="busquedaFreelance"),
    path('buscar/',views.buscar),
    path('leerFreelance',views.leerFreelance_view,name='leerFreelance'),
    path('leerContratador',views.leerContratador_view,name='leerContratador'),
    path('leerServicios',views.leerServicios_view,name='leerServicios'),
    path('eliminarFreelance/<freelance_nombre>/', views.eliminarFreelance, name="eliminarFreelance"),
    path('eliminarContratador/<contratador_nombre>/', views.eliminarContratador, name="eliminarContratador"),
    path('eliminarServicios/<servicio_nombreServicio>/', views.eliminarServicios, name="eliminarServicios"),
    path('editarFreelance/<freelance_nombre>/', views.editarFreelance, name="editarFreelance"),
    path('editarContratador/<contratador_nombre>/', views.editarContratador, name="editarContratador"),
    path('editarServicios/<contratador_nombre>/', views.editarServicios, name="editarServicios"),
    path('Freelance/list',views.FreelanceList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.FreelanceDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.FreelanceCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.FreelanceUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.FreelanceDelete.as_view(),name='Delete'),
    path('Contratador/list',views.ContratadorList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.ContratadorDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.ContratadorCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ContratadorUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ContratadorDelete.as_view(),name='Delete'),
    path('Servicios/list',views.ServiciosList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.ServiciosDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.ServiciosCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ServiciosUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ServiciosDelete.as_view(),name='Delete'),
    path('login',views.login_request, name="login"),
    path('register', views.register, name='register'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    path("my-protected-page/", views.MyProtectedView.as_view(), name="my_protected_page"),
    path("admin/", admin.site.urls),
    path('App1/',include('App1.urls'))
    
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
