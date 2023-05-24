from django.shortcuts import render
from App1.models import Curso
from django.http import HttpResponse

from App1.forms import EmpleadoForm, DepartamentoForm, PuestoForm
# Create your views here.
def inicio(request):
    return render (request, "App1/inicio.html")

def empleadoFormulario(request):
    if request.method=="POST":
        form= EmpleadoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            dni= informacion["dni"]
            nombre= informacion["nombre"]
            id_departamento= informacion["id_departamento"]
            id_puesto= informacion["id_puesto"]
            emple= Empleado(dni=dni, nombre=nombre, id_departamento=id_departamento, id_puesto=id_puesto)
            emple.save()
            return render(request, "App1/inicio.html" ,{"mensaje": "Se registró el empleado"})
        else:
            return render(request, "App1/empleadoFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario=EmpleadoForm()
        return render (request, "App1/empleadoFormulario.html", {"form": formulario})

def mostrarEmpleados(request):
    empleados=Empleado.objects.all()
    return render(request, "App1/mostrarEmpleados.html", {"empleados":empleados})

def busquedaEmpleado(request):
    return render(request, "App1/busquedaEmpleado.html")

def muestraBusquedaEmpleado(request):
    
    dni= request.GET["dni"]
    if dni!="":
        empleados= Empleado.objects.filter(dni=dni)
        return render(request, "App1/muestraBusquedaEmpleado.html", {"empleados": empleados})
    else:
        return render(request, "App1/busquedaEmpleado.html", {"mensaje": "Debe ingresar un DNI"})

def departamentosFormulario(request):
    if request.method=="POST":
        form= DepartamentoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            codigo= informacion["codigo"]
            nombre= informacion["nombre"]
            departamento= Departamento(codigo=codigo, nombre=nombre)
            departamento.save()
            return render(request, "App1/inicio.html" ,{"mensaje": "Se guardó el departamento"})
        else:
            return render(request, "App1/departamentosFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        formulario=DepartamentoForm()
        return render (request, "App1/departamentosFormulario.html", {"form": formulario}) 

def puestosFormulario(request):
    if request.method=="POST":
        form= PuestoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            codigo= informacion["codigo"]
            nombre= informacion["nombre"]
            departamento= informacion["departamento"]
            puesto= Puesto(codigo=codigo, nombre=nombre,departamento=departamento)
            puesto.save()
            return render(request, "App1/inicio.html" ,{"mensaje": "Puesto Guardado"})
        else:
            return render(request, "App1/puestosFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        formulario=PuestoForm()
        return render (request, "App1/puestosFormulario.html", {"form": formulario})           