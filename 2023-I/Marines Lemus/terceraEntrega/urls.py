"""
URL configuration for terceraEntrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import home, profile, registro, logeo, agregarAvatar, desloguear, client, cliente_editar, cliente_eliminar, product, producto_editar, producto_eliminar, seller, vendedor_editar, vendedor_eliminar, buscar
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('profile', profile, name='profile'),
    path('registro/',registro, name='registro'),
    path('logeo/',logeo, name='logeo'),
    path('agregarAvatar/',agregarAvatar, name='agregarAvatar'),
    path('desloguear/', desloguear, name='desloguear'),
    path('cliente/', client, name='cliente'),
    path('cliente_editar/<int:id_cliente>/', cliente_editar, name='cliente_editar'),
    path('cliente_eliminar/<int:id_cliente>/', cliente_eliminar, name='cliente_eliminar'),
    path('producto/', product, name='producto'),
    path('producto_editar/<int:id_producto>//', producto_editar, name='producto_editar'),
    path('producto_eliminar/<int:id_producto>//', producto_eliminar, name='producto_eliminar'),
    path('producto/', product, name='producto'),
    path('vendedor/', seller, name='vendedor'),
    path('vendedor_editar/<int:id_vendedor>/', vendedor_editar, name='vendedor_editar'),
    path('vendedor_eliminar/<int:id_vendedor>/', vendedor_eliminar, name='vendedor_eliminar'),
    path('busqueda/', buscar, name='buscar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
