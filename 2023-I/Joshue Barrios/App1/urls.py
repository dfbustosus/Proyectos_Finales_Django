from django.urls import path
from .views import *



urlpatterns = [

    path("", inicio, name="inicio"),

    path("empleadoFormulario/", empleadoFormulario, name="empleadoFormulario"),
    path("mostrarEmpleados/", mostrarEmpleados, name="mostrarEmpleados"),
    path("busquedaEmpleado/", busquedaEmpleado, name="busquedaEmpleado"),
    path("muestraBusquedaEmpleado/", muestraBusquedaEmpleado, name="muestraBusquedaEmpleado"),
    path("departamentosFormulario/", departamentosFormulario, name="departamentosFormulario"),
    path("puestosFormulario/", puestosFormulario, name="puestosFormulario"),


]
