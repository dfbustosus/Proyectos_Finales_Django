from django.shortcuts import render, redirect
from app1.models import Facciones,Hobbits, Orco, Elfo, Enano
from django.http import HttpResponse, QueryDict
from app1.forms import cursoformulario,Creacionformulario,UserRegisterForm,LoginForm
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.http import Http404



# Create your views here.
@login_required
def Faccion(request):
    return render(request, 'app1/faccion.html')

def Crear_Hobbits(request):
    if request.method == "POST":
            miFormulario = Creacionformulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                faccion = Hobbits( nombre = informacion ['nombre'], genero = informacion ['genero'], profesion = informacion ['profesion'])
                faccion.save()
                return render(request, "app1/faccion.html")
    else:
            miFormulario = Creacionformulario()
 
    return render(request, "app1/hobbits.html", {"miFormulario": miFormulario})

def Crear_Enanos(request):
    if request.method == "POST":
        miFormulario = Creacionformulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            faccion = Enano( nombre = informacion ['nombre'],genero = informacion ['genero'],profesion = informacion ['profesion'])
            faccion.save()
            return render(request, "app1/faccion.html")
    else:
        miFormulario = Creacionformulario()
 
        return render(request, "app1/enanos.html", {"miFormulario": miFormulario})

def Crear_Orcos(request):
    if request.method == "POST":
        miFormulario = Creacionformulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            faccion = Orco( nombre = informacion ['nombre'],genero = informacion ['genero'],profesion = informacion ['profesion'])
            faccion.save()
            return render(request, "app1/faccion.html")
    else:
        miFormulario = Creacionformulario()
 
        return render(request, "app1/orcos.html", {"miFormulario": miFormulario})


def Crear_Elfos(request):
    if request.method == "POST":
        miFormulario = Creacionformulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            faccion = Elfo( nombre = informacion ['nombre'],genero = informacion ['genero'],profesion = informacion ['profesion'])
            faccion.save()
            return render(request, "app1/faccion.html")
    else:
        miFormulario = Creacionformulario()
 
        return render(request, "app1/elfos.html", {"miFormulario": miFormulario})


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import UserRegisterForm

def login_register_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        register_form = UserRegisterForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("crear")
            else:
                return render(request, "app1/inicio.html", {'login_form': login_form, 'register_form': register_form, 'mensaje': 'Datos incorrectos'})

        elif register_form.is_valid():
            username = register_form.cleaned_data['username']
            register_form.save()
            messages.success(request, 'Usuario creado con éxito.')
            return render(request, "app1/inicio.html")

    else:
        login_form = AuthenticationForm()
        register_form = UserRegisterForm()

    return render(request, "app1/inicio.html", {'login_form': login_form, 'register_form': register_form})

def pagina_gaspar(request):
    return render(request, "app1/readme.html")


def log_out(request):
    return render(request, "app1/logout.html")

def leer_elfos(request):
    elfos = Elfo.objects.all()
    contexto={"elfos":elfos}
    return render(request,"app1/leerelfos.html",contexto)

def leer_hobbits(request):
    hobbit = Hobbits.objects.all()
    contexto={"hobbits":hobbit}
    return render(request,"app1/leerhobbits.html",contexto)

def leer_orcos(request):
    orcos = Orco.objects.all()
    contexto={"orcos":orcos}
    return render(request,"app1/leerorcos.html",contexto)

def leer_enanos(request):
    enanos = Enano.objects.all()
    contexto={"enanos":enanos}
    return render(request,"app1/leerenanos.html",contexto)

def eliminar_enano(request, enano_nombre):
    enano = Enano.objects.get(nombre=enano_nombre)
    enano.delete()
    enano = Enano.objects.all()
    contexto = {"enanos": enano}
    return render(request, "app1/leerenanos.html", contexto)

def eliminar_elfo(request, elfo_nombre):
    elfo = Elfo.objects.get(nombre=elfo_nombre)
    elfo.delete()
    elfo = Elfo.objects.all()
    contexto = {"elfos": elfo}
    return render(request, "app1/leerelfos.html", contexto)

def eliminar_hobbit(request, hobbit_nombre):
    hobbit = Hobbits.objects.get(nombre=hobbit_nombre)
    hobbit.delete()
    hobbit = Hobbits.objects.all()
    contexto = {"hobbits": hobbit}
    return render(request, "app1/leerhobbits.html", contexto)

def eliminar_orco(request, orco_nombre):
    orco = Orco.objects.get(nombre=orco_nombre)
    orco.delete()
    orco = Orco.objects.all()
    contexto = {"orcos": orco}
    return render(request, "app1/leerorcos.html", contexto)

from django.shortcuts import redirect

def editar_elfo(request, elfo_nombre):
    elfo = Elfo.objects.get(nombre=elfo_nombre)

    if request.method == 'POST':
        miFormulario = Creacionformulario(request.POST)
        
        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data

            elfo.nombre = informacion['nombre']
            elfo.genero = informacion['genero']
            elfo.profesion = informacion['profesion']
            elfo.save()

            return redirect('crear')

    else:
        miFormulario = Creacionformulario(initial={'nombre': elfo.nombre, 'genero': elfo.genero,
                                                   'profesion': elfo.profesion})
    
    return render(request, "app1/elfos.html", {"miFormulario": miFormulario, "elfo_nombre": elfo_nombre})


def editar_enano(request, enano_nombre):
    
    enano = Enano.objects.get(nombre=enano_nombre)
    
    if request.method == 'POST':
        
        miFormulario = Creacionformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  
            informacion = miFormulario.cleaned_data

            enano.nombre = informacion['nombre']
            enano.genero = informacion['genero']
            enano.profesion = informacion['profesion']
            enano.save()

            
            return redirect('crear')
    
    else:
       
        miFormulario = Creacionformulario(initial={'nombre': enano.nombre, 'genero': enano.genero,
                                                   'profesion': enano.profesion})
    
    return render(request, "app1/enanos.html", {"miFormulario": miFormulario, "enano_nombre": enano_nombre})


def editar_hobbit(request, hobbit_nombre):
    
    hobbit = Hobbits.objects.get(nombre=hobbit_nombre)
    
    if request.method == 'POST':
        
        miFormulario = Creacionformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  
            informacion = miFormulario.cleaned_data

            hobbit.nombre = informacion['nombre']
            hobbit.genero = informacion['genero']
            hobbit.profesion = informacion['profesion']
            hobbit.save()

            
            return redirect('crear')
    
    else:
       
        miFormulario = Creacionformulario(initial={'nombre': hobbit.nombre, 'genero': hobbit.genero,
                                                   'profesion': hobbit.profesion})
    
    return render(request, "app1/hobbits.html", {"miFormulario": miFormulario, "hobbit_nombre": hobbit_nombre})


def editar_orco(request, orco_nombre):
    
    orco = Orco.objects.get(nombre=orco_nombre)
    
    if request.method == 'POST':
        
        miFormulario = Creacionformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  
            informacion = miFormulario.cleaned_data

            orco.nombre = informacion['nombre']
            orco.genero = informacion['genero']
            orco.profesion = informacion['profesion']
            orco.save()

            
            return redirect('crear')
    
    else:
       
        miFormulario = Creacionformulario(initial={'nombre': orco.nombre, 'genero': orco.genero,
                                                   'profesion': orco.profesion})
    
    return render(request, "app1/orcos.html", {"miFormulario": miFormulario, "orco_nombre": orco_nombre})



