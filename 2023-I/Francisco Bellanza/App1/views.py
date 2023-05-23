from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from App1.forms import UserRegisterForm,UserEditForm
from App1.models import Avatar,Usuario
from django.contrib.auth.models import User

def inicio(request):
    return render(request, 'App1/padre.html')

def about(request):
    return render(request, 'App1/about.html')

def mas(request):
     return render(request, 'App1/mas.html')

def inicio_blog(request):
     return render(request, 'App1/inicioBlog.html')

def gastronomia(request):
     return render(request, 'App1/gastronomia.html')

def recetas(request):
     return render(request, 'App1/recetas.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/padreBlog.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/datosIncorrectos.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})


def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})

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

def leerUsuarios(request):
    usuarios= User.objects.all() # trae a todos los profesores
    contexto= {"usuarios": usuarios}
    return render(request, "App1/leerUsuarios.html",contexto)
















# Create your views here.
