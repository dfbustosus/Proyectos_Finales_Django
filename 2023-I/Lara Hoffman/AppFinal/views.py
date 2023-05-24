from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import *

def error_404(request, slug):
    return render(request, 'AppFinal/error404.html')

def admin_check(user):
    return user.is_superuser

class AdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

def inicio(request):
    return render(request, 'AppFinal/index.html')

def about(request):
    return render(request, "AppFinal/about.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Productos.objects.filter(nombre__icontains=nombre)
        return render(request, "AppFinal/index.html", {"productos":productos, "nombre":nombre})
    else:
        respuesta = "Ingrese el nombre del producto"
        return render(request, "AppFinal/index.html", {"respuesta":respuesta})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppFinal/index.html")
            else:
                mensajeError = "Error, datos incorrectos"
                return render(request, "AppFinal/login.html", {"mensajeError": mensajeError})
        else:
            mensajeForm = "Usuario o contraseña incorrectos"
            form = AuthenticationForm() #limpio los datos
            return render(request, "AppFinal/login.html", {"form":form, "mensajeForm": mensajeForm})
    
    form = AuthenticationForm()

    return render(request, "AppFinal/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            form = UserRegisterForm()
            mensaje = "Usuario creado con éxito"
            return render(request, "AppFinal/registro.html", {"form": form, "mensaje":mensaje})
        else:
            mensajeError = "Error al generar el usuario"
            return render(request, "AppFinal/registro.html", {"form": form, "mensaje":mensajeError})
    else:
        form = UserRegisterForm()

    return render(request, "AppFinal/registro.html", {"form": form})

class ProductosList(ListView):
    model = Productos
    context_object_name = "productos"
    template_name = "AppFinal/productos_list.html"

class ProductosDetail(DetailView):
    model = Productos
    template_name = "AppFinal/productos_detalle.html"

# @user_passes_test(admin_check)
class ProductosCreate(LoginRequiredMixin, AdminCheckMixin, CreateView):
    model = Productos
    template_name = "AppFinal/productos_create.html"
    success_url = "/productos/list"
    fields = '__all__'

# @user_passes_test(admin_check)
class ProductosUpdate(LoginRequiredMixin, AdminCheckMixin, UpdateView):
    model = Productos
    success_url = "/productos/list"
    fields = '__all__'

# @user_passes_test(admin_check)
class ProductosDelete(LoginRequiredMixin, AdminCheckMixin, DeleteView):
    model = Productos
    success_url = "/productos/list"

def leerMensajes(request):
    mensajes = Mensajes.objects.all()
    context = {"mensajes":mensajes}
    return render(request, "AppFinal/leerMensajes.html", context)

@login_required
def mensajes(request):
    if request.method == 'POST':
        miFormulario = MensajesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            pedido = Mensajes(nombre = info['nombre'], email = info['email'], comentario = info['comentario'])
            pedido.save()

            mensaje = "Su comentario ha sido añadido con éxito"
            miFormulario = MensajesFormulario()
            return render(request, "AppFinal/mensajes.html", {"miFormulario":miFormulario, "mensaje":mensaje})
    else:
        miFormulario = MensajesFormulario()
        return render(request, "AppFinal/mensajes.html", {"miFormulario":miFormulario})

@user_passes_test(admin_check)
@login_required
def eliminarMensaje(request, mensaje_nombre):
    mensaje = Mensajes.objects.get(nombre=mensaje_nombre)
    mensaje.delete()
 
    mensajes = Mensajes.objects.all()  # trae todos los mensajes
 
    contexto = {"mensajes": mensajes}
 
    return render(request, "AppFinal/leerMensajes.html", contexto)

@user_passes_test(admin_check)
@login_required
def editarMensaje(request, mensaje_nombre):
    mensaje = Mensajes.objects.get(nombre=mensaje_nombre)

    if request.method == 'POST':

        miFormulario = MensajesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data

            mensaje.nombre = info['nombre']
            mensaje.email = info['email']
            mensaje.comentario = info['comentario']

            mensaje.save()

            mensajes = Mensajes.objects.all()
            context = {"mensajes":mensajes}
        return render(request, "AppFinal/leerMensajes.html", context) #mejor que te lleve a otra pagina como el inicio
    else:
        miFormulario = MensajesFormulario(initial={'nombre': mensaje.nombre, 'email': mensaje.email, 'comentario': mensaje.comentario})

    return render(request, "AppFinal/editarMensajes.html", {"miFormulario": miFormulario, "mensaje_nombre": mensaje_nombre})

@login_required
def perfil(request):
    perfil, created = Perfiles.get_or_create_perfil(request.user)
    return render(request, 'AppFinal/perfil.html', {'perfil': perfil})

@login_required
def editarPerfil(request):
    perfil, created = Perfiles.get_or_create_perfil(request.user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        perfil_form = PerfilesFormulario(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('Perfil')

    else:
        user_form = CustomUserChangeForm(instance=request.user)
        perfil_form = PerfilesFormulario(instance=perfil)

    return render(request, 'AppFinal/editarPerfil.html', {'user_form': user_form, 'perfil_form': perfil_form})

