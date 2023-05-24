from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from app_1.models import *
from app_1.forms import *

""
# def (nombre definicion (self o request)):
#     variable= (traer de models la clase(diccionario))
#     variable.save()
#     algo mas que quieras agregar al codigo
#     return (retornar algo)
""



##-----Creacion de usuarios------##
def RegistroCliente(self):
    clienteReg= cliente(nombre="jime", apellido="adragna", email="jjindumentaria@gmail.com", contraseña="jimeteamo")
    clienteReg.save()
    texto= f"------->bienvenido {clienteReg.nombre} {clienteReg.apellido}"
    return HttpResponse(texto)
##-------------------------------##

##-----cargar stock--------------##
def CargarStock(self):
    prod= stock(producto="machimbre", cantidad="10", precio="1000" )
    prod.save()
    texto= f"Se ingreso {prod.producto}<br>Con una cantidad de:{prod.cantidad}.<br>Al precio de:{prod.precio}"
    return HttpResponse(texto)
##-------------------------------##

##--------Compra productos-------##
def CompraProducto(request):
    if request.method=="POST":
        miFormulario=ComprasUsuariof(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            lista=CompraUsuario(int(informacion["id"]), str(informacion["usuario"]), str(informacion["producto"]), str(informacion["cantidad"]))           
            
            lista.save()
            return render(request, "padre.html")
    else:
            miFormulario=ComprasUsuariof()

    return render(request, "Compras.html", {"miFormulario":miFormulario})

##-------------------------------##


def Plantilla(request):
    mihtml=open("C:/Users/Josefo/Desktop/CURSO CODERHOUSE/version Django 2.0/Proyecto_1/Proyecto_1/Templates/inicio.html")
    nombre="jose"
    diccionario={"nombre":nombre}
    plantilla=loader.get_template("inicio.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

##--------------cargar inicio ---------------##

def inicio(request):
    return render(request, "padre.html")




def RegUsuario(request):
    if request.method=="POST":
        miFormulario=RegistroUsuario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            lista=cliente(str(informacion["nombre"]), str(informacion["apellido"]), str(informacion["email"]), str(informacion["contraseña"]))           
            lista.save()
            return render(request, "padre.html")
    else:
            miFormulario=RegistroUsuario()

    return render(request, "RegUsuario.html", {"miFormulario":miFormulario})


def buscar(request):
     return render(request, "BUsuarios.html")




def busquedaUsuarios(request):
    usuario = request.GET.get("Usuario")
    
    if usuario:
        usuarios = cliente.objects.filter(nombre__icontains=usuario)
        return render(request, "ResultadoBusqueda.html", {"usuarios": usuarios})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def listaMateriales(request):
    if request.method == "POST":
        miFormulario = stocklista(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():  # Agrega paréntesis aquí
            informacion = miFormulario.cleaned_data
            lista = stock(int(informacion["id"]), str(informacion["producto"]), int(informacion["cantidad"]), int(informacion["precio"]))           
            lista.save()
            return render(request, "padre.html")
    else:
        miFormulario = stocklista()

    return render(request, "mostrarlista.html", {"miFormulario": miFormulario})


def leerLista(request):
    materiales=stock.objects.all()
    contexto={"materiales":materiales}
    return render (request, "listaMateriales.html", contexto)