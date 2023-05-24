from django.urls import path
from App1 import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('productos', views.productos, name="Productos" ),
    path('contacto', views.contacto, name="Contacto"),
    path('sobre_mi', views.sobre_mi, name="Sobre mi"),
    path('servicios', views.servicios, name="Servicios")
]