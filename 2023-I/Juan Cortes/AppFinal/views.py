from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppFinal.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "AppFinal/inicio.html")

def aboutme(request):

    return render(request, "AppFinal/aboutme.html")

# Vista Usuarios para guardar informacion
@login_required
def usuarios(request):
    if request.method == 'POST':
       miFormulario = UsuarioFormulario(request.POST) 
       print(miFormulario)

       if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'],email=informacion['email'],telefono=informacion['telefono'])

            usuario.save()

            respuesta = "Usuario registrado exitosamente"

            return render(request, "AppFinal/inicio.html", {"respuesta":respuesta})
    else:
       miFormulario = UsuarioFormulario()
    
    return render(request, "AppFinal/usuarios.html", {"miFormulario": miFormulario})

# Vista Vehiculos para guardar informacion
@login_required
def vehiculos(request):
    if request.method == 'POST':
       miFormulario = VehiculoFormulario(request.POST) 
       print(miFormulario)

       if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            vehiculo = Vehiculos(marca=informacion['marca'],tipo=informacion['tipo'],modelo=informacion['modelo'],precio=informacion['precio'] )

            vehiculo.save()
            
            respuesta = "Vehiculo registrado exitosamente"

            return render(request, "AppFinal/inicio.html", {"respuesta":respuesta})
    else:
       miFormulario = VehiculoFormulario()
    
    return render(request, "AppFinal/vehiculos.html", {"miFormulario": miFormulario})

# Vista Comentarios para guardar informacion
@login_required
def comentarios(request):
    if request.method == 'POST':
       miFormulario = ComentarioFormulario(request.POST) 
       print(miFormulario)

       if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            comentario = Comentario(nombre=informacion['nombre'],email=informacion['email'],telefono=informacion['telefono'],texto=informacion['texto'])

            comentario.save()

            respuesta = "Comentario registrado exitosamente"

            return render(request, "AppFinal/inicio.html", {"respuesta":respuesta})
    else:
       miFormulario = ComentarioFormulario()
    
    return render(request, "AppFinal/comentarios.html", {"miFormulario": miFormulario})

# Vista Usuarios para buscar Usuarios
def buscarusuario(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    
        return render(request, "AppFinal/usuarios.html", {"usuarios":usuarios,"nombre":nombre})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

# Vista Vehiculos para buscar Usuarios
def buscarvehiculo(request):
    
    if request.GET['marca']:
        marca = request.GET['marca']
        vehiculos = Vehiculos.objects.filter(marca__icontains=marca)
    
        return render(request, "AppFinal/vehiculos.html", {"vehiculos":vehiculos,"marca":marca})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

#Vista de menu de administrador
@login_required
def administrador_menu(request):
    return render(request, "AppFinal/administrador_menu.html")

#Vista de read lectura para usuarios
@login_required
def leerUsuarios(request):
    usuario = Usuario.objects.all()
    contexto = {"usuario":usuario}

    return render(request, "AppFinal/administrador_usuario.html", contexto)

#Vista de read lectura para vehiculos
@login_required
def leerVehiculos(request):
    vehiculo = Vehiculos.objects.all()
    contexto = {"vehiculo":vehiculo}

    return render(request, "AppFinal/administrador_vehiculo.html", contexto)

#Vista de read lectura para comentarios
@login_required
def leerComentarios(request):
    texto = Comentario.objects.all()
    contexto = {"texto":texto}

    return render(request, "AppFinal/administrador_comentarios.html", contexto)

#Vista de delete para Usuarios
@login_required
def eliminarUsuario(request, usuario_nombre):
    usuario = Usuario.objects.get(nombre=usuario_nombre)
    usuario.delete()

    usuario = Usuario.objects.all()
    contexto = {"usuario":usuario}

    return render(request, "AppFinal/administrador_usuario.html", contexto)

#Vista de delete para Vehiculos
@login_required
def eliminarVehiculo(request, vehiculo_marca):
    vehiculo = Vehiculos.objects.get(marca=vehiculo_marca)
    vehiculo.delete()

    vehiculo = Vehiculos.objects.all()
    contexto = {"vehiculo":vehiculo}

    return render(request, "AppFinal/administrador_vehiculo.html", contexto)

#Vista de delete para comentarios
@login_required
def eliminarComentario(request, texto_texto ):
    texto = Comentario.objects.get(texto=texto_texto)
    texto.delete()

    texto = Comentario.objects.all()
    contexto = {"texto":texto}

    return render(request, "AppFinal/administrador_comentarios.html", contexto)

#Vista para editar usuarios base de datos
@login_required
def editarUsuario(request, usuario_nombre):
    usuario = Usuario.objects.get(nombre=usuario_nombre)

    if request.method == 'POST':

        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.email = informacion['email']
            usuario.telefono = informacion['telefono']

            usuario.save()

            return render(request, "AppFinal/inicio.html")
    
    else:
        miFormulario = UsuarioFormulario(initial={'nombre':usuario.nombre, 'email':usuario.email, 'telefono':usuario.telefono})

    return render(request, "AppFinal/editarusuario.html", {"miFormulario":miFormulario, "usuario_nombre":usuario_nombre})

#Vista para editar Vehiculos
@login_required
def editarVehiculo(request, vehiculo_marca):
    vehiculo = Vehiculos.objects.get(marca=vehiculo_marca)

    if request.method == 'POST':

        miFormulario = VehiculoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            vehiculo.marca = informacion['marca']
            vehiculo.tipo = informacion['tipo']
            vehiculo.modelo = informacion['modelo']
            vehiculo.precio = informacion['precio']

            vehiculo.save()

            return render(request, "AppFinal/inicio.html")
    
    else:
        miFormulario = VehiculoFormulario(initial={'marca':vehiculo.marca, 'tipo':vehiculo.tipo, 'modelo':vehiculo.modelo, 'precio':vehiculo.precio})

    return render(request, "AppFinal/editarvehiculo.html", {"miFormulario":miFormulario, "vehiculo_marca":vehiculo_marca})

#Vista para editar comentarios
@login_required
def editarComentario(request, texto_texto):
    texto = Comentario.objects.get(texto=texto_texto)

    if request.method == 'POST':

        miFormulario = ComentarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            texto.nombre = informacion['nombre']
            texto.email = informacion['email']
            texto.telefono = informacion['telefono']
            texto.texto = informacion['texto']

            texto.save()

            return render(request, "AppFinal/inicio.html")
    
    else:
        miFormulario = ComentarioFormulario(initial={'nombre':texto.nombre, 'email':texto.email, 'telefono':texto.telefono, 'texto':texto.texto})

    return render(request, "AppFinal/editarcomentario.html", {"miFormulario":miFormulario, "texto_texto":texto_texto})

#Login de Usuarios 
def login_request(request):
    nickname = request.user

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            nickname = form.cleaned_data.get('username')
            keypass = form.cleaned_data.get('password')
            user = authenticate(username=nickname, password=keypass)
            
            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)

                if avatares:
                    respuesta = f"Bienvenido de nuevo {nickname}"
                    return render(request, "AppFinal/inicio.html", {'respuesta':respuesta, 'url':avatares[0].imagen.url})
                else:
                    respuesta = f"Bienvenido de nuevo {nickname}"
                    return render(request, "AppFinal/inicio.html", {'respuesta':respuesta})

        else:
                respuesta2 = f"Algo anda mal, revisa tus datos para poder ingresar"
                return render(request, "AppFinal/inicio.html", {'respuesta2':respuesta2})
            
    form = AuthenticationForm()

    return render(request, "AppFinal/login.html", {"form":form})      

#Registro de Usuarios  
def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            nickname = form.cleaned_data['username']

            form.save()
            respuesta = f"Usuario {nickname} creado exitosamente"
            return render(request, "AppFinal/inicio.html", {'respuesta':respuesta})
    else: 
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, "AppFinal/registro.html", {"form":form})

#Editar Usuarios de Django
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

            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "AppFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


#Añadir un avatar a los usuarios
@login_required
def agregarAvatar(request):
    nickname = request.user

    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()

            avatares = Avatar.objects.filter(user=request.user.id)
            respuesta = f"{nickname} Tu avatar ha sido actualizado"
            return render(request, "AppFinal/inicio.html", {"respuesta":respuesta, 'url':avatares[0].imagen.url})
    else:
        miFormulario = AvatarFormulario()
    
    return render(request, "AppFinal/agregarAvatar.html", {"miFormulario":miFormulario})
