from django.shortcuts import render
from App1.models import Contacto , Productos, Curso
from App1.forms import CursoFormulario
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def contacto(request):
    return render(request,'App1/contacto.html')
def productos(request):
    return render(request,'App1/productos.html')
def info(request):
    return render(request,'App1/info.html')
def save(request):
    return render(request,'App1/save.html')

def cursos(request):
    if request.method =='POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'App1/cursos.html', {"miFormulario": miFormulario})

def busquedaCurso(request):
    return render(request,'App1/busquedaCurso.html')

def buscar(request):
    if request.GET['curso']:
        curso = request.GET['curso']
        cursos= Curso.objects.filter(curso__icontains=curso)

        return render(request,'App1/resultadosBusqueda.html', {"cursos":cursos, "comisiones": curso })
    else:
        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)

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


def login1_request(request):
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
    return render(request, "App1/login1.html", {"form": form})


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
    