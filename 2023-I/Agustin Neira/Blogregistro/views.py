from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Avatar, Descripcion, Url
from .froms import Formulario_avatar, Formulario_url, Formulario_descripcion

from Blogregistro.froms import FormularioRegistro, Formulario_Edicion_Usuario, Formulario_url
from django.contrib.auth.decorators import login_required


# Create your views here.
def obtener_avatar(request):
    lista = Avatar.objects.filter(usuario=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = '/media/avatar/defecto.jfif'
    return avatar

def obtener_url(request):
    lista = Url.objects.filter(usuario=request.user)
    if len(lista) != 0:
        url = lista[0].url
    else:
        url = ''
    return url

def obtener_descripcion(request):
    lista = Descripcion.objects.filter(usuario=request.user)
    if len(lista) != 0:
        descripcion = lista[0].descripcion
    else:
        descripcion = ''
    return descripcion

def registro_usuario(request):
    if request.method == 'POST':
        form= FormularioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()                        
            return render(request, 'Blogapp/inicio.html', {'form': form, 'mensaje': 'Usuario creado exitosamente'})
        else:
            return render(request, 'Blogapp/Registro_usuario.html', {'form': form, 'mensaje': 'Error al crear el usuario'})   
    else:
        form= FormularioRegistro()
        return render(request, 'Blogapp/Registro_usuario.html', {'form': form})
        obtener_avatar(request)


def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion_usuario = form.cleaned_data
            username = informacion_usuario['username']
            password = informacion_usuario['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'Blogapp/inicio.html', {'mensaje': f'Bienvenido {username}', 'avatar': obtener_avatar(request)})
            else:
                return render(request, 'Blogapp/Login_usuario.html', {'form': form, 'mensaje': 'USUARIO o CONTRASEÑA incorrectos'})
        else:
            return render(request, 'Blogapp/Login_usuario.html', {'form': form, 'mensaje': 'USUARIO o CONTRASEÑA incorrectos'})
    else:
        form= AuthenticationForm()
        return render(request, 'Blogapp/Login_usuario.html', {'form': form})

@login_required
def editar_usuario(request):
    usuario=request.user
    if request.method == 'POST':
        form = Formulario_Edicion_Usuario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            return render(request, 'Blogapp/inicio.html', {'mensaje': f'{usuario.username} editado exitosamente', 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/editar_usuario.html', {'form': form, 'usuario': usuario.username, 'avatar': obtener_avatar(request)})
    else:
        form = Formulario_Edicion_Usuario(instance=usuario)
        return render(request, 'Blogapp/editar_usuario.html', {'form': form, 'usuario': usuario.username, 'avatar': obtener_avatar(request)})

@login_required
def perfil_usuario (request):
    usuario = request.user
    form = Formulario_Edicion_Usuario(instance=usuario)
    return render(request, 'Blogapp/perfil_usuario.html', {'avatar': obtener_avatar(request), 'url' : obtener_url(request), 'descripcion': obtener_descripcion(request), 'form': form})

@login_required
def agregar_avatar (request):
    if request.method == 'POST':
        form = Formulario_avatar(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(usuario=request.user, imagen=request.FILES['imagen'])
            avatarViejo= Avatar.objects.filter(usuario=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render (request, 'Blogapp/perfil_usuario.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Avatar agregado exitosamente'})
        else:
            return render (request, 'Blogapp/agregar_avatar.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Error al agregar el avatar'})
    else:
        form = Formulario_avatar()
        return render(request, 'Blogapp/agregar_avatar.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Agrega o modifica tu avatar'})

@login_required
def agregar_url (request):
    if request.method == 'POST':
        form = Formulario_url(request.POST)
        if form.is_valid():
            url = Url(usuario=request.user, url=request.POST['url'])
            urlViejo= Url.objects.filter(usuario=request.user)
            if len(urlViejo)>0:
                urlViejo[0].delete()
            url.save()
            return render (request, 'Blogapp/perfil_usuario.html', {'form': form, 'avatar': obtener_avatar(request), 'url' : obtener_url(request), 'mensaje': 'Url agregada exitosamente'})
        else:
            return render (request, 'Blogapp/agregar_url.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Error al agregar la url'})
    else:
        form = Formulario_url()
        return render(request, 'Blogapp/agregar_url.html', {'form': form, 'avatar': obtener_avatar(request)})

@login_required
def agregar_descripcion (request):
    if request.method == 'POST':
        form = Formulario_descripcion(request.POST)
        if form.is_valid():
            descripcion = Descripcion(usuario=request.user, descripcion=request.POST['descripcion'])
            descripcionVieja= Descripcion.objects.filter(usuario=request.user)
            if len(descripcionVieja)>0:
                descripcionVieja[0].delete()
            descripcion.save()
            return render (request, 'Blogapp/perfil_usuario.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Descripcion agregada exitosamente', 'descripcion': obtener_descripcion(request)})
        else:
            return render (request, 'Blogapp/agregar_descripcion.html', {'form': form, 'avatar': obtener_avatar(request), 'mensaje': 'Error al agregar la descripcion'})
    else:
        form = Formulario_descripcion()
        return render(request, 'Blogapp/agregar_descripcion.html', {'form': form, 'avatar': obtener_avatar(request)})