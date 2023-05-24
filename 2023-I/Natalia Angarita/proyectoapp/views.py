from django.shortcuts import render
from proyectoapp.models import Producto, Cliente, Vendedor
from django.http import HttpResponse
from proyectoapp.forms import productoFormulario, clienteFormulario, vendedorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


# Create your views here.
def inicio(request):
    return render(request, 'proyectoapp/inicio.html')

def productos(request):
    if request.method == 'post':
        miFormulario = productoFormulario(request.post)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(int(informacion['id']),str(informacion['categoria']),str(informacion['nombre']), int(informacion['precio'])) 
            producto.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = productoFormulario()
    return render(request,'proyectoapp/ProductoFormulario.html', {"miFormulario": miFormulario})


def cliente(request):
    if request.method == 'post':
        miFormulario = clienteFormulario(request.post)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),informacion['email'], informacion['profesion']) 
            cliente.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = clienteFormulario()
    return render(request,'proyectoapp/cliente.html', {"miFormulario": miFormulario})

def vendedor(request):
    if request.method == 'POST':
        miFormulario = vendedorFormulario(request.post)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            vendedor = Vendedor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),informacion['email'], informacion['categoria']) 
            vendedor.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = vendedorFormulario()
    return render(request,'proyectoapp/vendedor.html', {"miFormulario": miFormulario})


def producto(request):
    return render(request,'proyectoapp/producto.html')

def buscar(request):
     if request.GET['categoria']:
          categoria = request.GET['categoria']
          categorias= Producto.objects.filter(categoria__icontains= categoria)

          return render(request,'proyectoapp/inicio.html', {"productos":categorias, "comisiones": categoria })
     else:
          respuesta= "No se encontraron datos"

     return render(request,"proyectoapp/inicio.html",{"respuesta":respuesta})

def leerVendedor(request):
    vendedores = Vendedor.objects.all() #trae todos los profesores
    contexto= {"vendedores":vendedores}
    return render(request, "proyectoapp/leerVendedor.html",contexto) 


def eliminarVendedor(request, vendedor_nombre):
 
    vendedor = Vendedor.objects.get(nombre=vendedor_nombre)
    vendedor.delete()

    vendedores = Vendedor.objects.all()  # trae todos los profesores
    contexto = {"vendedores": vendedores}
    return render(request, "proyectoapp/leerVendedor.html", contexto)


def editarVendedor(request, vendedor_nombre):
    vendedor = Vendedor.objects.get(nombre=vendedor_nombre)
    if request.method == 'POST':
        miFormulario = vendedorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            vendedor.nombre = informacion['nombre']
            vendedor.apellido = informacion['apellido']
            vendedor.email = informacion['email']
            vendedor.categoria = informacion['categoria']

            vendedor.save()
            return render(request, "proyectoapp/inicio.html")

    else:
        miFormulario = vendedorFormulario (initial={'nombre': vendedor.nombre, 'apellido': vendedor.apellido, 'email': vendedor.email, 'categoria': vendedor.categoria})
    return render(request, "proyectoapp/vendedor.html", {"miFormulario": miFormulario, "vendedor_nombre": vendedor_nombre})

class ProductoList(ListView):
    model=Producto
    template_name="proyectoapp/productos_list.html"

class ProductoDetalle(DetailView):
    model=Producto
    template_name="proyectoapp/productos_detalle.html"

class ProductoCreacion(DetailView):
    model=Producto
    success_url="/proyectoapp/producto/list"
    fields = ['categoria', 'nombre', 'precio']

class ProductoUpdate(UpdateView):
    model=Producto
    success_url="/proyectoapp/producto/list"
    fields = ['categoria', 'nombre', 'precio']

class ProductoDelete(DeleteView):
    model=Producto
    success_url="/proyectoapp/producto/list"
   