from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import ProductoFormu,ClienteFormu,ProveedorFormu
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def sobremi(request):
    return render(request, 'App1/sobremi.html')
@login_required
def Producto(request):
    return render(request,'App1/producto.html')
@login_required
def Cliente(request):
    return render(request,'App1/cliente.html')
@login_required
def Proveedor(request):
    return render(request,'App1/proveedor.html')

                            # <<<<<<<<<<<< FORMULARIOS PRODUCTO >>>>>>>>>>>>>
def Producto(request):
    if request.method =='POST':
        miFormulario=ProductoFormu(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=producto(int(informacion['id']),str(informacion['nombre']),int(informacion['cantidad']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=ProductoFormu()
    return render(request, 'App1/producto.html', {"miFormulario": miFormulario})
                        
                            # <<<<<<<<<<<< FORMULARIOS CLIENTE >>>>>>>>>>>>>
def Cliente(request):
    if request.method =='POST':
        miFormulario=ClienteFormu(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),str(informacion['email']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=ClienteFormu()
    return render(request, 'App1/cliente.html', {"miFormulario": miFormulario})
   
                        # <<<<<<<<<<<< FORMULARIOS PROVEEDOR >>>>>>>>>>>>>
def Proveedor(request):
    if request.method =='POST':
        miFormulario=ProveedorFormu(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso = proveedor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),str(informacion['email']),int(informacion['cuil']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario= ProveedorFormu()
    return render(request, 'App1/cliente.html', {"miFormulario": miFormulario})
                            

                            # <<<<<<<<<<<< BUSQUEDA PRODUCTO >>>>>>>>>>>>>
def BusquedaProducto(request):
     return render(request,'App1/busquedaProducto.html')
#Buscador
def buscar(request):
     if request.GET ['i_cantidad']:
        cant = request.GET ['i_cantidad']
        resultado= producto.objects.filter(nombre__icontains=cant)
        return render(request, 'App1/resultadobusqueda.html', {"resultado":resultado}) # Llamo a la busqueda
     else:
          respuesta= "No se encontraron datos para mostrar"
     return HttpResponse (respuesta)     

def leerProveedor(request):
      proveedores = proveedor.objects.all() #trae todos los proveedores
      contexto= {"proveedores":proveedores} 
      return render(request, "App1/leerproveedor.html",contexto)

def eliminarProveedor(request, proveedores_cuit):
    proveedores = proveedor.objects.get(cuit=proveedores_cuit)
    proveedores.delete()
    # vuelvo al menú
    profesores = proveedor.objects.all()  # trae todos los profesores 
    contexto = {"proveedores": proveedores}
    return render(request, "App1/leerProveedor.html", contexto)

def editarProveedor(request, proveedores_cuit):
    # Recibe el nombre del profesor que vamos a modificar
    proveedores = proveedor.objects.get(cuit=proveedores_cuit)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProveedorFormu(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            proveedores.nombre = informacion['nombre']
            proveedores.apellido = informacion['apellido']
            proveedores.email = informacion['email']
            proveedores.cuit = informacion['cuil']
            proveedores.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProveedorFormu(initial={'nombre': proveedores.nombre, 'apellido': proveedores.apellido,
                                                   'email': proveedores.email, 'cuit': proveedores.cuit})
    # Voy al html que me permite editar
    return render(request, "App1/editarProveedor.html", {"miFormulario": miFormulario, "proveedores_cuit": proveedores_cuit})

# CBV

from django.views.generic import ListView
class ProductoList(ListView):
    model =producto
    template_name='/App1/producto_list.html'

from django.views.generic.detail import DetailView

class ProductoDetalle(DetailView):
    model=producto
    template_name= "App1/producto_detalle.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ProductoCreacion(CreateView):
    model=producto
    success_url="/App1/producto/list"
    fields= ['nombre','cantidad']

from django.views.generic.edit import UpdateView

class ProductoUpdate(UpdateView):
    model=producto
    success_url= "/App1/producto/list"
    fields=['nombre','cantidad']

from django.views.generic.edit import DeleteView

class ProductoDelete(DeleteView):
    model=producto
    success_url="/App1/producto/list"

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})

from App1.forms import UserRegisterForm

def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})

from App1.forms import ProductoFormu, ClienteFormu, UserRegisterForm, UserEditForm,ProveedorFormu
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "App1/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

from App1.models import proveedor, cliente, Avatar,producto


from App1.models import Avatar
def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'pibot.html', {'user_avatar': user_avatar})

from django.contrib.auth.models import User
from .forms import AvatarFormulario
@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App1/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})


