from django.shortcuts import render , HttpResponse ,redirect
from tienda.models import Prodcto
from .carrito import Carrito
from django.contrib import messages
# Create your views here.

def tienda(request):
    
    productos = Prodcto.objects.all()
    
    return render(request, "tienda/home.html", {"productos" : productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Prodcto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("home")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Prodcto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("home")
    
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Prodcto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    messages.success(request, 'Carrito Vaciado Correctamente')
    return redirect("home")

def comprar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    messages.success(request, 'Compra Realizada Correctamente')
    return redirect("home")