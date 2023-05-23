
from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('productos', login_required (views.productos), name="Productos"),
    path('vendedores',login_required(views.cargarproducto),name='Vendedores'),
    
#busqueda de productos
    path('busquedaProducto',views.busquedaProducto,name="BusquedaProducto"),
    path('buscar/',views.buscar),
    path('productos/', views.productos, name='productos'),
    path('busquedaProducto', views.busqueda_producto, name='busquedaProducto'),

#lista de busqueda, edición y borrado de productos
    path('producto/list',views.ProductoList.as_view(),name='List'),
    path(r'^(?P<pk>/d+)$', views.ProductoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>/d+)$',views.ProductoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>/d+)$',views.ProductoDelete.as_view(),name='Delete'),
    path('listaProducto',views.ProductoList.as_view(), name='listaProducto'),

#Login, Logout y Register

    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout',  LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),

#Acerca de mí
    path('acercaDeMi/', views.about, name='acerca_de_mi'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

#agregar
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    

   
]