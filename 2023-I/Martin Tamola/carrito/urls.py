from django.urls import path
from tienda import views
from carrito import views

urlpatterns = [
    path("", views.tienda, name='carrito'),
    path("agregar/<int:producto_id>", views.agregar_producto, name='agregar'),
    path("eliminar/<int:producto_id>", views.eliminar_producto, name='eliminar'),
    path("restar/<int:producto_id>", views.restar_producto, name='restar'),
    path("limpiar/", views.limpiar_carrito, name='limpiar'),
    path("comprar/", views.comprar, name='comprar'),
    
]