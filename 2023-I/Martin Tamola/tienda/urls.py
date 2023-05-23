from django.urls import path , include
from tienda import views
from tienda.views import ProfileUpdate

urlpatterns = [
    path("", views.home, name='home'),
    path("contacto/", views.contacto, name='contacto'),
    path("galeria/", views.galeria, name='galeria'),
    path("sobremi/", views.sobremi, name='sobremi'),
    path("agregar-producto/", views.agregar_producto, name='agregar_producto'),
    path("agregar-marca/", views.agregar_marca, name='agregar_marca'),
    path("listar-contactos/", views.listar_contactos, name='listar_contactos'),
    path("listar-productos/", views.listar_productos, name='listar_productos'),
    path("modificar-productos/<id>/", views.modificar_producto, name='modificar_productos'),
    path("eliminar-producto/<id>/", views.eliminar_producto, name='eliminar_producto'),
    path("detalle-producto/<id>/", views.detalle_producto, name='detalle_producto'),
    path("listar-marcas/", views.listar_marcas, name='listar_marcas'),
    path("modificar-marca/<id>/", views.modificar_marca, name='modificar_marca'),
    path("eliminar-marca/<id>/", views.eliminar_marca, name='eliminar_marca'),
    path("registro/", views.registro, name="registro"),
    path("carrito/", include('carrito.urls')),
    path("accounts/profile/", ProfileUpdate.as_view(), name='profile'),
]