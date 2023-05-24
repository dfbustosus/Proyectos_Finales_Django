from django.urls import path

from .views import ViewRegisto, cerrar_sesion, logear



urlpatterns = [

    path('', ViewRegisto.as_view(), name='Autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('logear', logear, name='logear'),


]
