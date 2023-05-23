from django.shortcuts import render
from AppEntrega.models import *
from django.http import HttpResponse
from AppEntrega.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from AppEntrega.forms import RecetaFormulario, NewsLetterFormulario, UserRegisterForm, UserEditForm
from django.contrib.auth.models import User

def inicio(request):
    return render(request,'AppEntrega/inicio.html')
def recetas(request):
    return render(request,'AppEntrega/recetas.html')
def newsletter(request):
    return render(request,'AppEntrega/newsletter.html')

#Funcion para ingresar recetas a la base de datos 
@login_required
def recetas(request):
    if request.method == "POST":
        miformulario= RecetaFormulario(request.POST)
        print(miformulario)
        
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            nombre =Recetas(int(informacion['id']),str(informacion['nombre']),(informacion['ingredientes']),str(informacion['descripcion']))
            nombre.save()
            return render(request,'AppEntrega/inicio.html')
    else:
            miformulario=RecetaFormulario()
        
    return render(request,'AppEntrega/recetas.html', {'miformulario':miformulario})

  # Generamos el la funcion para la recoleccion de datos para  la creacion de usuario    
     
 
#inscribir los datos para el newsletter
def newsletter(request):
    if request.method == "POST":
        miformulario = NewsLetterFormulario(request.POST)
        print(miformulario)
        
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            news = NewsLetter(int(informacion['id']),str(informacion['nombre']),str(informacion['email']))
            news.save()
            return render(request,'AppEntrega/inicio.html')
    else:
        miformulario=NewsLetterFormulario()
        
    return render(request,'AppEntrega/newsletter.html', {'miformulario':miformulario})

def busquedaReceta(request):
    return render(request, 'AppEntrega/busquedaReceta.html')


def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        recetas = Recetas.objects.filter(nombre__icontains=nombre)
        
        return render(request,'AppEntrega/resultadosbusqueda.html',{"nombre":nombre, "recetas":recetas, "descripcion":recetas})
    else:
        respuesta = "No fue posible encontrar la receta que buscas"
    return HttpResponse(respuesta) 
        
    

#Vista y edición de recetas
@login_required
def leerRecetas(request):
    recetas = Recetas.objects.all()
    contexto = {"recetas":recetas}
    return render(request,"AppEntrega/leerRecetas.html", contexto)
 
@login_required       
def eliminarRecetas(request, receta_nombre):
    receta = Recetas.objects.get(nombre=receta_nombre)
    receta.delete()
    recetas = Recetas.objects.all() 
    contexto = {"recetas": recetas}
    return render(request, "AppEntrega/leerRecetas.html", contexto)

@login_required
def editarReceta(request,receta_nombre):
    receta = Recetas.objects.get(nombre =receta_nombre)
    if request.method =='POST':
        miformulario = RecetaFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion =miformulario.cleaned_data
            receta.nombre= informacion['nombre']
            receta.ingredientes =informacion['ingredientes']
            receta.descripcion = informacion['descripcion']
            receta.save()
            return render(request,"AppEntrega/inicio.html")
            

    else:
        miformulario = RecetaFormulario(initial={'nombre':receta.nombre, 'ingredientes':receta.ingredientes, 'descripcion':receta.descripcion})
        
    return render(request,"AppEntrega/editarReceta.html",{"miformulario":miformulario, "receta_nombre":receta_nombre})





#Registro e ingreso 
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            passw  = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=passw)
            if user is not None:
                login(request, user)
                return render(request, "AppEntrega/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppEntrega/inicio.html", {"mensaje":"Alguno o más datos están incorrectos"})
        else:
            return render(request, "AppEntrega/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AppEntrega/login.html", {"form": form})
    
from AppEntrega.forms import UserRegisterForm

def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppEntrega/inicio.html" ,  {"mensaje":"Usuario creado satisfactoriamente"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AppEntrega/registro.html" ,  {"form":form})
  


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miformulario = UserEditForm(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "AppEntrega/inicio.html")
    else:

        miformulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppEntrega/editarPerfil.html", {"miformulario": miformulario, "usuario": usuario})

@login_required
def inicioAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppEntrega/inicio.html',{"url":avatares[0].imagen.url})

def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'padre.html', {'user_avatar': user_avatar})

@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            FormularioAvatar= AvatarFormulario(request.POST, request.FILES) 
            if FormularioAvatar.is_valid():   
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=FormularioAvatar.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "AppEntrega/inicio.html")
      else: 
            FormularioAvatar= AvatarFormulario()
      return render(request, "AppEntrega/agregarAvatar.html", {"FormularioAvatar":FormularioAvatar})
  
def aboutMe(request):
    return render(request,'AppEntrega/aboutMe.html')

    

       