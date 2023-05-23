
from typing import Any,Dict
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from App1.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import EditProfileForm
from .models import Debate, Opinion
from django.contrib.auth.models import User
from .forms import AvatarFormulario
from App1.models import Avatar
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate


def inicio(request):
    return render(request,'App1/inicio.html')
def kobe(request):
    return render(request,'App1/kobe.html')
def consejos(request):
    return render(request,'App1/consejos.html')

def login(request):
    if request.method == "POST":
        print('entro al post', request)
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contrasenia=form.cleaned_data['password']
            user= authenticate(username=usuario,password=contrasenia)
            if user is not None:
                login(request,user)
                return render(request,"App1/inicio.html",{"message": f"Bienvenido {usuario}"})
            else:
                return render(request,"App1/inicio.html",{"message": "Datos incorrectos"})
        else:
            return render(request,"App1/inicio.html",{"message": "Formulario erroneo"})
    print("Solicitud de inicio de sesión recibida.")
    form=AuthenticationForm()
    return render(request,"App1/login.html",{"form":form})

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"App1/inicio.html",{"mensaje":"Usuario Creado  :)"})
    else:
        form=UserRegisterForm()
    return render(request,"App1/register.html",{"form":form})

def miperfil(request):
    return render(request,"App1/miperfil.html")

@login_required
def editarPerfil(request):
    return render(request, "App1/editarPerfil.html")

@login_required
def editarPerfil(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('editarPerfil')
        else:
            messages.error(request, 'Por favor corrija los errores abajo.')
    else:
        user_form = EditProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }

    return render(request, 'App1/editarPerfil.html', context)

    return render(request, 'App1/editarPerfil.html', context)

def foro(request):
    return render(request,"App1/foro.html")


from django.shortcuts import render, redirect
from .models import Debate 
@login_required
def nuevo_debate(request):
    if request.method == 'POST':
        
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        tema = request.POST['tema']
        opinion = request.POST['opinion']
        nuevo_debate = Debate(nombre=nombre, apellido=apellido, tema=tema, opinion=opinion)
        nuevo_debate.save()    
        return redirect('debatenuevoexitoso')

    return render(request, 'App1/nuevodebate.html')
def debatenuevoexitoso(request):
     return render(request, 'App1/debatenuevoexitoso.html')


def ver_debates(request):
    debates = Debate.objects.all()
    return render(request, 'App1/ver_debates.html', {'debates': debates, 'user': request.user})

def opinar_sobre_debate(request, debate_id):
    debate = Debate.objects.get(id=debate_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        mensaje = request.POST.get('contenido')
        
        if nombre and apellido and mensaje:
            opinion = Opinion(debate=debate, nombre=nombre, apellido=apellido, mensaje=mensaje)
            opinion.save()
            return render(request,'App1/opinion_exitosa.html')
        else:
            messages.error(request, 'Por favor, completa todos los campos del formulario.')

    return render(request, 'App1/opinar_sobre_debate.html', {'debate': debate})

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        return render(request, 'App1/inicio.html', {"url": avatares[0].imagen.url})
    else:
        return render(request, 'App1/inicio.html')
    
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) 
            if miFormulario.is_valid():   
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App1/inicio.html") 
      else: 
            miFormulario= AvatarFormulario() 
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})

from django.shortcuts import render
from .models import Debate, Opinion

def ver_opiniones(request, debate_id):
    debate = Debate.objects.get(id=debate_id)
    opiniones = debate.opiniones.all()
    
    context = {
        'debate': debate,
        'opiniones': opiniones
    }
    
    return render(request, 'App1/ver_opiniones.html', context)

def opinion_exitosa(request):
    return render(request,"App1/opinion_exitosa")