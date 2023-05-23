from django.urls import path 
from App1 import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('', views.inicio , name="inicio"), # Incio de la paguina
    path('Producto',login_required(views.Producto), name="Producto"), # Producto
    path('Cliente',login_required (views.Cliente),name="Cliente"),# Cliente
    path('Proveedores', login_required(views.Proveedor),name="Proveedor"),# Proveedores
    path('proveedorformulario',views.Proveedor,name='proveedorformulario'),
    path('BusquedaProducto',views.BusquedaProducto,name="BusquedaProducto"),
    path('buscar/',views.buscar),
    path('leerProvedor',views.leerProveedor,name='leerProveedor'),
    path('eliminarProveedor/<proveedores_cuit>/', views.eliminarProveedor, name="EliminarProveedor"),
    path('editarProveedor/<proveedores_cuit>/', views.editarProveedor, name="EditarProveedor"),

    path('producto/list',views.ProductoList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ProductoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ProductoDelete.as_view(),name='Delete'),
    path('login/',views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('sobremi', views.sobremi, name="sobremi"),
]