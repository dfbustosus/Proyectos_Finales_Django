from django.shortcuts import render, redirect
from App1.models import Producto , Avatar
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from App1.forms import ProductoFormulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , DeleteView , UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .forms import AvatarFormulario
from datetime import datetime




# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
@login_required
def productos(request):
    return render(request,'App1/productos.html')
@login_required
def vendedores(request):
    return render(request,'App1/vendedores.html')





@login_required
def productos(request):
    if request.method =='POST':
        miFormulario=ProductoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            producto=Producto(int(informacion['id']),str(informacion['nombre']),int(informacion['codigodeventa']), informacion['descripcion'])
            producto.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=ProductoFormulario()
    return render(request, 'App1/productos.html', {"miFormulario": miFormulario})



@login_required
def busquedaProducto(request):
     return render(request,'App1/busquedaProducto.html')
@login_required
def buscar(request):
     if request.GET['producto']:
          producto = request.GET['producto']
          productos = Producto.objects.filter(codigodeventa__icontains=producto)

          return render(request,'App1/resultadosBusqueda.html', {"productos":productos, "producto_buscado": producto})
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)

              

#Funciones para editar, ver y

def busqueda_producto(request):
    return render(request, 'busquedaProducto.html')


class ProductoList(ListView):
    model =Producto 
    template_name='/App1/producto_list.html'

class ProductoDetalle(DetailView):
    model=Producto 
    template_name= "App1/producto_detalle.html"

class ProductoCreacion(CreateView):
    model=Producto
    success_url="/App1/producto/list"
    fields= ['nombre','codigodeventa']

from django.views.generic.edit import UpdateView

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = "/App1/producto/list"
    fields = ['nombre', 'codigodeventa', 'descripcion', 'imagen']

    def form_valid(self, form):
        if 'imagen' in form.cleaned_data and form.cleaned_data['imagen'] is None:
            del form.cleaned_data['imagen']
        return super().form_valid(form)

class ProductoDelete(DeleteView):
    model=Producto
    success_url="/App1/producto/list"


def lista_producto(request):
    return render(request, 'producto_list.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

#Login
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
            return render(request, "App1/inicio.html", {"mensaje":"Usuario o contraseña incorrecta"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})

#Registro
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

def about(request):
    return render(request, 'App1/acercaDeMi.html', {})


# Vista de editar el perfil

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            # Actualizar la contraseña si se proporcionó una nueva
            nueva_contraseña = informacion['password1']
            if nueva_contraseña:
                usuario.set_password(nueva_contraseña)
                usuario.save()

            return render(request, "App1/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




#Prueba para vendedores

@login_required
def cargarproducto(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            imagen = request.FILES.get('imagen', None)
            producto = Producto(
                id=int(informacion['id']),
                nombre=str(informacion['nombre']),
                codigodeventa=int(informacion['codigodeventa']),
                descripcion=informacion['descripcion']
            )
            if imagen:
                producto.imagen = imagen
            producto.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario = ProductoFormulario()
    return render(request, 'App1/vendedores.html', {"miFormulario": miFormulario})


# AVATAR




def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'padre.html', {'user_avatar': user_avatar})


@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return redirect('Inicio') #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})


#Fecha y Hora


def fecha_hora_actual(request):
    now = datetime.now()
    context = {
        'fecha_actual': now.date(),
        'hora_actual': now.time(),
    }
    return render(request, 'fecha_hora.html', context)