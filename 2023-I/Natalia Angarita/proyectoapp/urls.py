from django.urls import path
from proyectoapp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('producto', views.producto, name="Producto"),
    path('cliente', views.cliente, name="Cliente"),
    path('vendedor', views.vendedor, name="Vendedor"),
    path('productos', views.productos, name="productos"),
    path('buscar/',views.buscar),
    path('leerVendedor', views.leerVendedor, name = "leerVendedor"),
    path('eliminarVendedor/<vendedor_nombre>/', views.eliminarVendedor, name="EliminarVendedor"),
    path('editarVendedor/<vendedor_nombre>/', views.editarVendedor, name="EditarVendedor"),

    path('producto/list',views.ProductoList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ProductoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ProductoDelete.as_view(),name='Delete')


]